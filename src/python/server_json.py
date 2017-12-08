"""
Basic web server with flask
Listening: 127.0.0.1 (redirection 0.0.0.0 => 127.0.0.1 because of vagrant)
Port: 8000
"""
import sys
from flask import Flask, json, jsonify, request
from flask_cors import CORS

from dialog_flow import request_dialog_flow
from excel_query import qui_est_responsable, qui_travaille_sur_projet

app = Flask("python")
# Accept cross origins request
cors = CORS(app, resources={r"*": {"origins": "*"}})

# Route to speak to the chat bot
@app.route('/get_simple_message', methods=['GET', 'POST'])
def api_root():
    if request.method == 'POST':
        if request.form['user_msg']:
            print(request.form['user_msg'], file=sys.stderr)
            ai_response = request_dialog_flow(msg=request.form['user_msg'])
            if "qui_est_responsable" in ai_response:
                personne = ai_response["qui_est_responsable"]["responsable"]
                responsable = qui_est_responsable(personne)
                return jsonify(
                    message="Le responsable de %s est %s" % (personne, responsable),
                    format="simple_message",
                    robot=True
                )
            elif "qui_travaille_sur_projet" in ai_response:
                projet = ai_response["qui_travaille_sur_projet"]["project"]
                personnes = qui_travaille_sur_projet(projet)
                if not personnes:
                    return jsonify(
                        message="Personne ne travaille sur le porjet %s." % projet,
                        format="simple_message",
                        robot=True
                    )
                return jsonify(
                    message="Les personnes qui travaillent sur le projet %s sont:\n%s" % (projet, ', '.join(p.nom for p in personnes)),
                    format="simple_message",
                    robot=True
                )

    # TODO Sinon renvoyer un message par défaut
    return jsonify(
        message="Je n'ai pas compris la question",
        format="simple_message",
        robot=True
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
