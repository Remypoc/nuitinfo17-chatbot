import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ChatBot, { Loading } from 'react-simple-chatbot';

// Source: https://github.com/LucasBassetti/react-simple-chatbot
const theme = {
  background: '#f5f8fb',
  fontFamily: 'Helvetica Neue',
  headerBgColor: '#EF6C00',
  headerFontColor: '#fff',
  headerFontSize: '15px',
  botBubbleColor: '#EF6C00',
  botFontColor: '#fff',
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
      msg_format: 'classic'
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

    function readyStateChange() {
      if (this.readyState === 4) {
        const data = JSON.parse(this.responseText);
        if (data.robot && data.format == "simple_message") {
          self.setState({ loading: false, result: data.messagen, msg_format='classic' });
        } else if (data.robot && data.format == "url_message") {
          self.setState({ loading: false, result: data.message, msg_format='url'});
        } else {
          self.setState({ loading: false, result: 'Not found.' });
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

    if (msg_format == 'simple_message') {
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
    } else if (msg_format == 'url') {
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
}

BotResponse.propTypes = {
  steps: PropTypes.object,
  triggerNextStep: PropTypes.func,
};

BotResponse.defaultProps = {
  steps: undefined,
  triggerNextStep: undefined,
};

const App = () => (
  <ChatBot
    steps={[
      {
        id: '1',
        message: 'Salut, qui es-tu ?',
        trigger: 'wait_user_msg',
      },
      {
        id: 'wait_user_msg',
        user: true,
        trigger: '3',
      },
      {
        id: '3',
        component: <BotResponse />,
        asMessage: true,
        trigger: 'wait_user_msg'
      },
    ]}
  />
);

export default App;