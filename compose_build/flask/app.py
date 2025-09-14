# Importa o pacote principal do Flask
import flask

# Importa classes e funções específicas do Flask
# Flask -> classe principal para criar a aplicação web
# jsonify -> transforma dicionários Python em JSON na resposta HTTP
# request -> permite acessar dados da requisição (GET, POST, headers, body, params, etc.)
from flask import Flask, jsonify, request

# Importa a biblioteca requests para fazer chamadas HTTP externas
import requests

# Importa a biblioteca que permite integração com MySQL no Flask
import flask_mysqldb

# Importa a classe MySQL para criar a conexão com o banco de dados
from flask_mysqldb import MySQL

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Ativa o modo de debug: mostra erros detalhados e reinicia o servidor automaticamente ao salvar alterações
app.config['DEBUG'] = True

# Configurações do banco de dados MySQL
app.config['MYSQL_HOST'] = 'db'  # Host do MySQL (quando rodando em container Docker)
app.config['MYSQL_USER'] = 'root'                  # Usuário do banco
app.config['MYSQL_PASSWORD'] = 'root'             # Senha do banco
app.config['MYSQL_DB'] = 'flaskdocker'              # Nome do banco de dados

# Inicializa a conexão MySQL com a aplicação Flask
mysql = MySQL(app)

# Define uma rota "/" que responde apenas a requisições GET
@app.route('/', methods=['GET'])
def index():
    # Faz uma requisição GET para a API externa randomuser.me
    data = requests.get('https://randomuser.me/api')
    
    # Retorna os dados JSON obtidos da API diretamente para o cliente
    return data.json()

# Define uma rota "/inserthost" que responde apenas a requisições POST
@app.route('/inserthost', methods=['POST'])
def inserthost():
    # Faz uma requisição GET para a API externa e já transforma a resposta em JSON
    data = requests.get('https://randomuser.me/api').json()
    
    # Pega o primeiro nome do usuário gerado pela API
    user = data['results'][0]['name']['first']  

    # Cria um cursor para executar comandos SQL
    cur = mysql.connection.cursor()
    
    # Insere o nome do usuário na tabela "users"
    cur.execute("INSERT INTO users(name) VALUES(%s)", (user,))
    
    # Confirma a transação no banco de dados
    mysql.connection.commit()
    
    # Fecha o cursor
    cur.close() 

    # Retorna o nome inserido como resposta da requisição
    return  "Usuario inserido: " + user

# Ponto de entrada do programa
# Se o arquivo for executado diretamente, inicia o servidor Flask
if __name__ == '__main__':
    # Roda o servidor Flask
    # host="0.0.0.0" -> deixa o servidor acessível externamente (não apenas localhost)
    # debug=True -> ativa modo debug
    # port="5000" -> servidor escutando na porta 5000
    app.run(host="0.0.0.0", debug=True, port="5000")
