from flask import Flask, request, jsonify
import json

app = Flask(__name__)

alunos = [
    {
        "Alunos": "Pedro vasconcelos",
        "Idade": 25,
        "Sala": "3C",
        "Professor": "valter almeida"
    },
    {
        "Alunos": "Nicolas de lima",
        "Idade": 27,
        "Sala": "3B",
        "Professor": "Bruno correia"
    },
    {
        "Alunos": "Amanda babtista",
        "Idade": 25,
        "Sala": "3C",
        "Professor": "valter almeita"
    },
     {
        "Alunos": "Arthur de alencar",
        "Idade": 27,
        "Sala": "3B",
        "Professor": "Bruno correia"
    }

]

alunos_json = json.dumps(alunos)

@app.route('/')
def home():
    return 'Para ver a lista de alinos entre no caminho (/alunos)'

@app.route('/alunos', methods=["GET"])
def lista():
    return alunos_json, 200

if __name__ == "__main__":
    app.run(debug=True)

