# Usa a imagem oficial do Python 3 como base
# Isso já inclui o interpretador Python 3 instalado e pronto para uso
FROM python:3

# Define o diretório de trabalho dentro do container como /app
# A partir daqui, todos os comandos RUN, COPY e CMD serão relativos a /app
WORKDIR /app

# Instala as dependências do projeto usando o gerenciador pip
# Flask -> framework web para criar a aplicação
# requests -> biblioteca para fazer requisições HTTP externas
# flask_mysqldb -> biblioteca para conectar Flask com MySQL
RUN pip install Flask requests flask_mysqldb

# Copia todos os arquivos do diretório atual (host) para o diretório /app dentro do container
# Isso inclui o app.py, arquivos Python e outros recursos do projeto
COPY . .

# Expõe a porta 5000 do container
# Permite que outras aplicações ou o host acessem o container através desta porta
# OBS: apenas documenta a porta, não cria mapeamento automaticamente
EXPOSE 5000

# Define o comando padrão que será executado quando o container iniciar
# Aqui ele executa o arquivo app.py usando Python
CMD ["python", "app.py"]
