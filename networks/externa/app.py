# Importa o pacote principal do Flask
import flask

# Importa classes e funções específicas do Flask
# Flask -> cria a aplicação
# jsonify -> transforma dicionários Python em JSON na resposta
# request -> permite acessar dados da requisição (headers, body, params, etc.)
from flask import Flask, jsonify, request

# Importa a biblioteca requests para fazer chamadas HTTP externas
import requests

# Cria a aplicação Flask
app = Flask(__name__)

# Ativa o modo de debug (mostra erros detalhados e recarrega o servidor automaticamente ao salvar alterações)
app.config['DEBUG'] = True

# Define uma rota "/" que responde apenas a requisições GET
@app.route('/', methods=['GET'])
def index():
    # Faz uma requisição GET para a API randomuser.me (gera dados de usuário aleatórios)
    data = requests.get('https://randomuser.me/api')
    
    # Retorna o JSON da resposta diretamente para o cliente
    return data.json()

# Ponto de entrada do programa
# Se o arquivo for executado diretamente (python app.py), inicia o servidor Flask
if __name__ == '__main__':
    # Roda o servidor Flask acessível em todas as interfaces de rede (0.0.0.0),
    # com debug ativado, e escutando na porta 5000
    app.run(host="0.0.0.0", debug=True, port="5000")
