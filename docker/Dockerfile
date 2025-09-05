# Usa a imagem oficial do Node.js como base
# (pega a última versão disponível do Node)
FROM node

# Define o diretório de trabalho dentro do container como /app
# Todos os próximos comandos serão executados a partir dessa pasta
WORKDIR /src

# Copia os arquivos package.json e package-lock.json (se existir)
# Isso permite instalar dependências antes de copiar o resto do código
COPY package*.json ./

# Instala as dependências do projeto com o npm
RUN npm install

# Copia todos os arquivos do projeto para dentro do container
# (inclusive o código-fonte, que vai sobrescrever o que já estava lá)
COPY . .

# Expõe a porta 3000 do container (a mesma usada no app Node)
EXPOSE 3000

# Comando que será executado quando o container iniciar
# Nesse caso, inicia a aplicação Node rodando o app.js
CMD ["node", "app.js"]
