// 📌 Como instalar e rodar este projeto com Node.js:

// 1. Baixe e instale o Node.js no site oficial: https://nodejs.org
//    → escolha a versão LTS (recomendada para a maioria dos usuários).
//    → durante a instalação, marque a opção "Add to PATH".

// 2. Após instalar, abra o terminal e verifique as versões:
//    node -v   (mostra a versão do Node.js)
//    npm -v    (mostra a versão do npm, o gerenciador de pacotes)

// 3. Crie uma pasta para o projeto e entre nela:
//    mkdir meu-projeto
//    cd meu-projeto

// 4. Inicie um novo projeto Node.js:
//    npm init -y

// 5. Instale o Express (framework necessário para este código):
//    npm install express

// 6. Crie um arquivo chamado index.js e copie o código abaixo.

// 7. Rode o projeto:
//    node index.js

// 8. Abra no navegador: http://localhost:3000
//    → você verá a mensagem "Hello World!"

// -------------------------------------------------------------

const express = require('express'); // importa o express
const app = express();              // cria a aplicação
const port = 3000;                  // define a porta do servidor

// rota principal (GET /)
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// inicia o servidor
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
