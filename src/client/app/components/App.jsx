import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ChatBot, { Loading } from 'react-simple-chatbot';

// Source: https://github.com/LucasBassetti/react-simple-chatbot

class DBPedia extends Component {
  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      result: '',
      trigger: false,
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
          self.setState({ loading: false, result: data.message });
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
            {
              !trigger &&
              <button
                onClick={() => this.triggetNext()}
              >
                Search Again
              </button>
            }
          </div>
        }
      </div>
    );
  }
}

DBPedia.propTypes = {
  steps: PropTypes.object,
  triggerNextStep: PropTypes.func,
};

DBPedia.defaultProps = {
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
        component: <DBPedia />,
        asMessage: true,
        trigger: '1'
      },
    ]}
  />
);

export default App;