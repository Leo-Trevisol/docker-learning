# Usa a imagem oficial do Python 3 como base
FROM python:3

# Atualiza o gerenciador de pacotes e instala dependências adicionais
# python3-pip: gerenciador de pacotes Python
# python3-dev: bibliotecas e headers para desenvolvimento Python
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# Define o diretório de trabalho dentro do container como /app
WORKDIR /app

# Instala a biblioteca Flask dentro do container
RUN pip install Flask

# Copia todos os arquivos do diretório atual (host) para o diretório /app do container
COPY . . 

# Expõe a porta 5000 do container para que possa ser acessada externamente
EXPOSE 5000

# Define o comando que será executado quando o container iniciar
# Neste caso, roda o arquivo app.py usando Python
CMD [ "python", "./app.py" ]

# -----------------------------
# Fluxo para Deployment e Service no Kubernetes:
# 1. Criar o Deployment:
#    kubectl create deployment flask-deployment --image=leonardotrevisol/flask-kub-project
#
# 2. Verificar pods criados:
#    kubectl get pods
#
# 3. Expor o Deployment com um Service do tipo LoadBalancer:
#    kubectl expose deployment flask-deployment --type=LoadBalancer --port=5000
#
# 4. Verificar Service e IP externo:
#    kubectl get services
#
# 5. Acessar a aplicação pelo navegador ou curl usando o IP/porta fornecidos
