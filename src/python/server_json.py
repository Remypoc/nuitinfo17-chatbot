"""
Basic web server with flask
Listening: 127.0.0.1 (redirection 0.0.0.0 => 127.0.0.1 because of vagrant)
Port: 8000
"""
import sys
from flask import Flask, json, jsonify, request
from flask_cors import CORS

from dialog_flow import request_dialog_flow
from excel_query import (qui_est_responsable, qui_travaille_sur_projet,
                        qui_sait_faire_competence, comment_joindre_responsable_projet, 
                        comment_contacter_personne, competences_liees_au_projet, 
                        role_de_personne, de_quoi_personne_est_responsable)

app = Flask("python")
# Accept cross origins request
cors = CORS(app, resources={r"*": {"origins": "*"}})

# Route to speak to the chat bot
@app.route('/get_simple_message', methods=['GET', 'POST'])
def api_root():
    message = "Je n'ai pas compris la question"
    format_message="simple_message"
    if request.method == 'POST':
        if request.form['user_msg']:
            print(request.form['user_msg'], file=sys.stderr)
            ai_response = request_dialog_flow(msg=request.form['user_msg'])
            if "qui_est_responsable" in ai_response:
                personne = ai_response["qui_est_responsable"]["name"]
                responsable = qui_est_responsable(personne)
                message="Le responsable de %s est %s" % (personne, responsable),
            elif "qui_travaille_sur_projet" in ai_response:
                projet = ai_response["qui_travaille_sur_projet"]["project"]
                personnes = qui_travaille_sur_projet(projet)
                if not personnes:
                    message="Personne ne travaille sur le projet %s." % projet
                else:
                    message="Les personnes qui travaillent sur le projet %s sont:\n%s" % (projet, ', '.join(p.nom for p in personnes)),
            elif "qui_sait_faire_competence" in ai_response:
                competence = ai_response["qui_sait_faire_competence"]["competence"]
                personnes = qui_sait_faire_competence(competence)
                if not personnes:
                    message = "Personne ne sait faire %s." % competence
                else:
                    message = "Les personnes qui sachent faire %s sont: \n%s" % (competence, ', '.join(p.nom for p in personnes))
            elif "comment_joindre_responsable_projet" in ai_response:
                projet = ai_response['comment_joindre_responsable_projet']['projet']
                personne = comment_joindre_responsable_projet(projet)
                if not personne:
                    message = "Je n'ai pas réussi à trouver ce projet !"
                else:
                    message = "Vous pouvez joindre %s, responsable du projet %s à %s" % (personne.nom, personne.projet, personne.contact)
                pass
            elif "comment_contacter_personne" in ai_response:
                nom = ai_response['comment_contacter_personne']['nom']
                personne = comment_contacter_personne(nom)
                if not personne:
                    message = "Je n'ai pas réussi à trouver cette personne !"
                else:
                    message = "Vous pouvez joindre %s à %s" % (personne.nom, personne.contact)
                pass
            elif "competences_liees_au_projet" in ai_response:
                projet = ai_response['competences_liees_au_projet']['projet']
                competences = competences_liees_au_projet(projet)
                if not competences:
                    message = "Je n'ai pas réussi à trouver ce projet !"
                else:
                    message = "Les compétences liées au projet %s sont : %s" % (projet, ', '.join(competences))
                pass
            elif "role_de_personne" in ai_response:
                nom = ai_response['role_de_personne']['nom']
                role = role_de_personne(nom)
                if not role:
                    message = "Je n'ai pas réussi à trouver cette personne !"
                else:
                    message = "Le role de %s est %s" % (nom, role)
                pass
            elif "de_quoi_personne_est_responsable" in ai_response:
                nom = ai_response['de_quoi_personne_est_responsable']['nom']
                responsable_de = de_quoi_personne_est_responsable(nom)
                if not responsable_de:
                    message = "%s n'est responsable de rien !" % nom
                else:
                    message = "%s est responsable de %s" % (nom, ', '.join(responsable_de))
                pass
            

    # TODO Sinon renvoyer un message par défaut
    return jsonify(
        message=message,
        format=format_message,
        robot=True
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
