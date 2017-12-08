"""
Google dialog flow chatbot connection
"""

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
import apiai
import json

CLIENT_ACCESS_TOKEN = 'cf4346d73c6a458a9da7c471d9c904dc'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

def request_dialog_flow(msg=None):
    if not msg:
        return None
    request = ai.text_request()
    request.lang = "fr"
    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
    request.query = msg
    response = request.getresponse()
    response_str = response.read().decode("utf-8")
    with open("response.json", "w") as file:
        file.write(response_str)
    response_json = json.loads(response_str)
    return {
        response_json["result"]["metadata"]["intentName"]: response_json["result"]["parameters"]
    }