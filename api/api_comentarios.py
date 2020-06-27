#Importando bibliotecas
import os
from flask import Flask, jsonify, request

#Instânciando o Flask
application = Flask(__name__)

#Lista para receber os comentários
comentarios = []

#Inserindo um novo comentário
@application.route('/comentar', methods=['POST'])
def comentar():
    inserir = request.get_json()
    comentarios.append(inserir) #Salvando o dado em memória
    return jsonify(inserir), 201

#Consultando todos os comentários
@application.route('/consultar', methods=['GET'])
def consultar():
    return jsonify(comentarios), 200

#Declarando valores que serão utilizados para subir a aplicação em container
if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)