import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ChatBot, { Loading } from 'react-simple-chatbot';
import { ThemeProvider } from 'styled-components';

// Source: https://github.com/LucasBassetti/react-simple-chatbot
const theme = {
  background: '#fffff',
  fontFamily: "Helvetica Neue",
  headerBgColor: '#003181',
  headerFontColor: '#ffd300',
  headerFontSize: '15px',
  botBubbleColor: '#003181',
  botFontColor: '#ffd300',
  userBubbleColor: '#fff',
  userFontColor: '#4a4a4a',
};

class BotResponse extends Component {
  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      result: '',
      trigger: false,
      msg_format: 'classic',
    };

    this.triggetNext = this.triggetNext.bind(this);
  }

  componentWillMount() {
    const self = this;
    const { steps } = this.props;
    const user_msg = "user_msg=" + encodeURI(steps.wait_user_msg.value);

    const queryUrl = 'http://localhost:8000/get_simple_message';


    const xhr = new XMLHttpRequest();
    xhr.open('POST', queryUrl, true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.addEventListener('readystatechange', readyStateChange);
    xhr.send(user_msg);
    this.props.update_history(user_msg, this.props.chatBot);

    function readyStateChange() {
      if (this.readyState === 4) {
        const data = JSON.parse(this.responseText);
        if (data.robot && data.format == "simple_message" || data.format == "url_message") {
          self.setState({ loading: false, result: data.message, msg_format: 'classic' });
        } else {
          self.setState({ loading: false, result: 'Not found.', msg_format: 'classic' });
        }
      }
    }
  }

  triggetNext() {
    this.setState({ trigger: true }, () => {
      this.props.triggerNextStep();
    });
  }

  render() {
    const { trigger, loading, result } = this.state;
      return (
        <div style={{ width: '100%' }}>
          { loading ? <Loading /> : result }
          {
            !loading &&
            <div
              style={{
                textAlign: 'center',
                marginTop: 20,
              }}
            >
            </div>
          }
        </div>
      );
  }
}

BotResponse.propTypes = {
  steps: PropTypes.object,
  triggerNextStep: PropTypes.func,
};

BotResponse.defaultProps = {
  steps: undefined,
  triggerNextStep: undefined,
};


class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      history: []
    };

    this.update_history = this.update_history.bind(this);
  }

  update_history(new_message, chatBot) {
    this.setState(prevState => ({
      history: [...prevState.history, new_message]
    }));
  }

  render() {
    return (
      <ThemeProvider theme={theme}>
        <ChatBot
          headerTitle="Nuit de l'info 2017 - ChatBot LCL"
          placeholder="Ecrivez votre message ..."
          botDelay="200"
          userDelay="200"
          width="100%"
          recognitionLang='fr'
          steps={[
            {
              id: '1',
              message: 'Bonjour, je suis le bot le plus classe du monde. Mais qui es-tu ?',
              trigger: 'wait_user_msg',
            },
            {
              id: 'wait_user_msg',
              user: true,
              trigger: '3',
            },
            {
              id: '3',
              component: <BotResponse update_history={this.update_history} />,
              asMessage: true,
              trigger: 'wait_user_msg'
            },
          ]}
        />
      </ThemeProvider>
    );
  }
}

export default App;