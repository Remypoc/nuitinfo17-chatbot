"""
Basic web server with flask
Listening: 127.0.0.1 (redirection 0.0.0.0 => 127.0.0.1 because of vagrant)
Port: 8000
"""

import sys
from flask import Flask, json, jsonify, request
from flask_cors import CORS

from dataLoader import DataLoader

dataLoader = DataLoader()
persons = dataLoader.getAllPersons()

app = Flask("python")
cors = CORS(app, resources={r"*": {"origins": "*"}})


def quiTravailleSurX(projet):
    personnes_concernnees = []
    global persons
    for person in persons:
        if person.projet == projet:
            personnes_concernnees.append(person)
    print(personnes_concernnees, file=sys.stderr)
    return personnes_concernnees

@app.route('/get_simple_message', methods=['GET', 'POST'])
def api_root():
    response = "Je n'ai pas compris la question"
    if request.method == 'POST':
        if request.form['user_msg']:
            print(request.form['user_msg'], file=sys.stderr)
            tokens = request.form['user_msg'].split()
            if tokens[0] == "Qui":
                personnes = quiTravailleSurX(tokens[3] + " " + tokens[4])
                print(personnes, file=sys.stderr)
                if not personnes:
                    response = "Personne ne travaille sur %s %s." % (tokens[3], tokens[4])
                else:
                    response = "Voici les personnes qui travaillent sur %s %s: " % (tokens[3], tokens[4]) + personnes[0].nom

    return jsonify(
        message=response,
        format="simple_message",
        robot=True
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
