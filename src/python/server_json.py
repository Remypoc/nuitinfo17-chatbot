"""
Basic web server with flask
Listening: 127.0.0.1 (redirection 0.0.0.0 => 127.0.0.1 because of vagrant)
Port: 8000
"""

from flask import Flask, json, jsonify
from flask_cors import CORS

app = Flask("python")
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/get_simple_message')
def api_root():
    return jsonify(
        message="Non pas Alexandre ! Noooooooon.....",
        format="simple_message",
        robot=True
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
