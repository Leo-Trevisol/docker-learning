# Usa a imagem oficial do Python 3 como base
FROM python:3

# Define o diretório de trabalho dentro do container como /app
# Tudo a partir daqui será executado dentro dessa pasta
WORKDIR /app

# Instala as dependências necessárias usando o pip
# Nesse caso: Flask (framework web) e requests (para chamadas HTTP)
RUN pip install Flask requests

# Copia todos os arquivos do diretório atual (host) para o /app no container
COPY . .

# Expõe a porta 5000 do container
# Isso não abre a porta automaticamente, mas documenta que o container usa essa porta
EXPOSE 5000

# Define o comando padrão que será executado quando o container iniciar
# Aqui vai rodar o app Python usando "python app.py"
CMD ["python", "app.py"]
