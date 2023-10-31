from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def hello():
    return "/songs"

@app.route('/songs', methods=['POST'])
def way_with_post():
    data = request.get_json()
    return jsonify({'message': 'Dados recebidos com sucesso!'})

@app.route('/songs', methods=['PUT'])
def putt():
    data = request.get_json()
    return jsonify({'message': 'Dados recebidos com sucesso!'})

@app.route('/songs')

def ler_csv():
    csvfile = "spf.csv"

    dados = []

    with open(csvfile, mode='r', newline='', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        for  row in reader: 
            dados.append(row)
            


    return jsonify(dados)


if __name__ == "__main__":
    app.run()

    