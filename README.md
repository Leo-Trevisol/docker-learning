<h1 align="center">🐳 Docker - Fundamentos e Prática</h1>

<p align="center">
  Repositório com exemplos práticos para aprender e dominar o uso do <strong>Docker</strong>, 
  desde os fundamentos até gerenciamento de containers, imagens, redes e orquestração.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Docker-20.10+-blue?logo=docker" />
  <img src="https://img.shields.io/badge/Containers-Management-green?logo=docker" />
  <img src="https://img.shields.io/badge/Images-Build-orange?logo=docker" />
  <img src="https://img.shields.io/badge/Volumes-Persistence-yellow?logo=docker" />
  <img src="https://img.shields.io/badge/Networks-Connectivity-lightgrey?logo=docker" />
  <img src="https://img.shields.io/badge/Compose-Stack-blueviolet?logo=docker" />
  <img src="https://img.shields.io/badge/Kubernetes-Orchestration-blue?logo=kubernetes" />
  <img src="https://img.shields.io/badge/Swarm-Orchestration-lightgrey?logo=docker" />
  <img src="https://img.shields.io/badge/YAML-Config-red?logo=yaml" />
  <img src="https://img.shields.io/badge/Linux-Terminal-black?logo=linux" />
</p>

<hr/>

<section id="o-que-voce-vai-aprender">
  <h2>📚 O que você vai aprender aqui?</h2>

  <ul>
    <li><strong>⚙️ Fundamentos do Docker</strong><br/>
      - O que é Docker e para que serve<br/>
      - Instalação e configuração<br/>
      - Principais comandos do Docker
    </li>

    <li><strong>📦 Containers e Imagens</strong><br/>
      - Criação e execução de containers<br/>
      - Criação, atualização e gerenciamento de imagens<br/>
      - Copiando arquivos de/para containers com <code>docker cp</code><br/>
      - Publicação de imagens no Docker Hub
    </li>

    <li><strong>🗄️ Gerenciamento de Recursos</strong><br/>
      - Volumes e persistência de dados<br/>
      - Bind Mount<br/>
      - Criação e utilização de networks<br/>
      - Conexão externa: host ↔ containers e entre containers
    </li>
  </ul>

  <h3>🛠️ Docker Compose</h3>
  <ul>
    <li>Gerenciamento de múltiplos containers</li>
    <li>Criação de ambientes completos com Compose</li>
    <li>Exemplos de arquivos <code>docker-compose.yml</code> e boas práticas</li>
  </ul>

  <h3>🚀 Projetos Práticos</h3>
  <ul>
    <li>Aplicações em <strong>PHP</strong>, <strong>Python</strong>, <strong>JavaScript</strong> e outras tecnologias</li>
    <li>Estruturação de projetos dockerizados</li>
    <li>Exemplos step-by-step para dockerizar aplicações reais</li>
  </ul>

  <h3>📑 YAML para Docker e Kubernetes</h3>
  <ul>
    <li>Estrutura e sintaxe do YAML</li>
    <li>Modo declarativo vs. imperativo</li>
    <li>Exemplos de manifests para Compose e Kubernetes</li>
  </ul>

  <h3>🌐 Orquestração com Docker Swarm</h3>
  <ul>
    <li>Instalação e configuração do Swarm</li>
    <li>Criação e atualização de projetos no Swarm</li>
    <li>Replicação de serviços</li>
    <li>Uso de Docker Compose no Swarm</li>
  </ul>

  <h3>☸️ Orquestração com Kubernetes</h3>
  <ul>
    <li>Instalação e uso do Minikube</li>
    <li>Conceitos fundamentais de Kubernetes (Pods, Services, Deployments)</li>
    <li>Criação e gerenciamento de projetos</li>
    <li>Escalabilidade e orquestração de containers</li>
  </ul>

  <h3>💻 Linux e Terminal</h3>
  <ul>
    <li>Essenciais de terminal/Linux</li>
    <li>Aplicação prática no uso do Docker</li>
    <li>Comandos úteis para debug e administração</li>
  </ul>
</section>

<section id="sobre-docker">
  <h2>🐳 O que é Docker?</h2>
  <p>
    O <strong>Docker</strong> é uma plataforma de código aberto que permite criar, empacotar,
    distribuir e executar aplicações em <strong>containers</strong>. 
    Os containers são unidades isoladas que contêm tudo o que um aplicativo precisa para funcionar:
    código, bibliotecas, dependências e variáveis de ambiente.
  </p>
  <p>
    A principal vantagem do Docker é a <strong>portabilidade</strong> e a <strong>consistência</strong>:
    um container pode ser executado da mesma forma em diferentes sistemas operacionais ou servidores,
    evitando problemas de incompatibilidade entre ambientes.
  </p>

  <h2>✨ Por que usar Docker?</h2>
  <ul>
    <li><strong>Portabilidade:</strong> seu aplicativo roda igual em qualquer lugar (Linux, Windows, macOS, nuvem etc.).</li>
    <li><strong>Agilidade:</strong> ambientes prontos em segundos, sem necessidade de instalar dependências manualmente.</li>
    <li><strong>Escalabilidade:</strong> fácil replicação e distribuição de serviços.</li>
    <li><strong>Eficiência:</strong> containers compartilham recursos do sistema, consumindo menos que máquinas virtuais.</li>
    <li><strong>Colaboração:</strong> facilita o trabalho em equipe, garantindo que todos usem o mesmo ambiente.</li>
    <li><strong>Compatibilidade com a nuvem:</strong> suporte nativo em provedores como AWS, Azure e Google Cloud.</li>
    <li><strong>Integração com orquestradores:</strong> funciona perfeitamente com <em>Docker Swarm</em> e <em>Kubernetes</em>.</li>
  </ul>
</section>

<section id="matrix-from-hell">
  <h2>🔥 O que é a <em>Matrix from Hell</em> no Docker?</h2>
  <p>
    A <strong>Matrix from Hell</strong> é um termo usado para descrever quando um projeto cria uma
    quantidade enorme de combinações de ambientes em pipelines de CI/CD.
    Isso acontece ao testar múltiplas versões de linguagens, bancos de dados e sistemas operacionais,
    gerando uma matriz de builds quase impossível de gerenciar manualmente.
  </p>

  <h3>⚠️ Problemas comuns</h3>
  <ul>
    <li>Crescimento <em>exponencial</em> de combinações de testes.</li>
    <li>Aumento do tempo e custo de execução na pipeline.</li>
    <li>Dificuldade para manter e diagnosticar falhas.</li>
  </ul>

  <h3>✅ Como o Docker ajuda</h3>
  <ul>
    <li><strong>Dockerfiles parametrizados:</strong> permite variar versões sem criar vários arquivos.</li>
    <li><strong>Docker Compose:</strong> facilita orquestrar ambientes complexos.</li>
    <li><strong>Imagens pré-buildadas:</strong> reduzem tempo de build e tornam o fluxo mais eficiente.</li>
    <li><strong>Execução isolada:</strong> cada ambiente roda em containers separados, evitando conflitos.</li>
  </ul>

  <h3>📎 Resumo</h3>
  <p>
    A <em>Matrix from Hell</em> acontece quando o número de combinações de ambientes cresce de forma
    descontrolada. O <strong>Docker</strong> ajuda a reduzir essa complexidade,
    garantindo ambientes consistentes e mais fáceis de reproduzir.
  </p>
</section>

<section id="docker-start">
  <h2>⚡ Iniciando o Docker</h2>
  <p>
    Antes de rodar qualquer container, é importante garantir que o 
    <strong>Docker Engine</strong> esteja em execução.
  </p>

  <h3>🪟 No Windows</h3>
  <p>
    No Windows, o Docker roda através do <strong>Docker Desktop</strong>.
    Ele precisa estar aberto para que os <code>docker</code> funcionem no terminal
    (PowerShell, Cmder ou WSL).
  </p>
  <ul>
    <li>Abra o <em>Docker Desktop</em> manualmente pelo menu iniciar.</li>
    <li>Ou, inicie pelo terminal:
      <pre><code>"C:\Program Files\Docker\Docker\Docker Desktop.exe"</code></pre>
    </li>
    <li>Recomenda-se ativar a opção <em>"Start Docker Desktop when you log in"</em> nas configurações,
      para que o Docker suba automaticamente junto com o Windows.</li>
  </ul>

  <h3>🐧 No Linux</h3>
  <p>
    No Linux, o Docker é instalado como um serviço de sistema. 
    Você pode controlá-lo com o <code>systemctl</code>.
  </p>
  <ul>
    <li>Para iniciar o serviço:
      <pre><code>sudo systemctl start docker</code></pre>
    </li>
    <li>Para habilitar o Docker na inicialização:
      <pre><code>sudo systemctl enable docker</code></pre>
    </li>
    <li>Para verificar se está rodando:
      <pre><code>systemctl status docker</code></pre>
    </li>
  </ul>

  <h3>✅ Dica</h3>
  <p>
    Após iniciar o Docker (seja no Windows ou Linux), teste se está funcionando corretamente com:
  </p>
  <pre><code>docker run --rm hello-world</code></pre>
  <p>
    Se o comando rodar e mostrar a mensagem de boas-vindas, o Docker está funcionando 🚀.
  </p>
</section>

<section id="docker-authentication">
  <h2>🔐 Autenticação no Docker Hub e Gerenciamento de Imagens</h2>

  <h3>🔑 Autenticando-se no Docker Hub</h3>
  <p>
    Para publicar ou baixar imagens privadas do <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>, 
    você precisa autenticar-se com sua conta Docker. Isso também é necessário para acessar imagens públicas 
    se você atingir os limites de uso gratuito ou tiver configurado autenticação obrigatória.
  </p>
  <ul>
    <li>
      <strong>Faça login no Docker Hub:</strong><br>
      Use o comando abaixo para autenticar-se:
      <pre><code>docker login</code></pre>
      Você será solicitado a inserir seu nome de usuário e senha do Docker Hub. Após o login bem-sucedido, 
      suas credenciais serão armazenadas localmente para uso futuro.
    </li>
    <li>
      <strong>Verifique sua conta:</strong><br>
      Antes de usar o Docker Hub, certifique-se de que seu e-mail foi verificado. Acesse 
      <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>, faça login, e verifique seu e-mail 
      na seção de configurações da conta. Caso não tenha recebido o e-mail de verificação, solicite um novo 
      em <strong>Account Settings > Security</strong>.
    </li>
    <li>
      <strong>Usando um token de acesso pessoal (opcional):</strong><br>
      Se sua conta tem autenticação de dois fatores (2FA) ativada, você precisará usar um token de acesso 
      pessoal (PAT) em vez de sua senha:
      <ul>
        <li>Vá para <strong>Account Settings > Security > Personal Access Tokens</strong> no Docker Hub.</li>
        <li>Crie um novo token e copie-o.</li>
        <li>Use o token como senha ao executar:
          <pre><code>docker login -u seu-usuario</code></pre>
        </li>
      </ul>
    </li>
    <li>
      <strong>Logout:</strong><br>
      Para fazer logout do Docker Hub:
      <pre><code>docker logout</code></pre>
    </li>
  </ul>

  <h3>⬆️ Publicando Imagens no Docker Hub (Push)</h3>
  <p>
    Após criar sua própria imagem, você pode publicá-la no Docker Hub para compartilhá-la com outros ou 
    usá-la em diferentes máquinas. Antes de fazer o push, a imagem precisa estar nomeada com o formato 
    <code>seu-usuario/nome-imagem:tag</code>.
  </p>
  <ul>
    <li>
      <strong>Construa a imagem com um nome apropriado:</strong><br>
      Ao criar a imagem com <code>docker build</code>, inclua seu nome de usuário do Docker Hub:
      <pre><code>docker build -t seu-usuario/meu-app:1.0 .</code></pre>
      Aqui, <code>seu-usuario</code> é seu nome de usuário no Docker Hub, <code>meu-app</code> é o nome 
      do repositório, e <code>1.0</code> é a tag da versão.
    </li>
    <li>
      <strong>Ou renomeie uma imagem existente:</strong><br>
      Se a imagem já foi criada com um nome diferente, use o comando <code>docker tag</code> para renomeá-la:
      <pre><code>docker tag meu-app-node seu-usuario/meu-app:1.0</code></pre>
    </li>
    <li>
      <strong>Faça o push da imagem:</strong><br>
      Após garantir que você está autenticado com <code>docker login</code>, publique a imagem:
      <pre><code>docker push seu-usuario/meu-app:1.0</code></pre>
      Isso enviará a imagem para o Docker Hub, onde ela ficará disponível no seu repositório público ou privado.
    </li>
    <li>
      <strong>Verifique no Docker Hub:</strong><br>
      Acesse <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>, vá para seus repositórios, 
      e confirme que a imagem <code>seu-usuario/meu-app:1.0</code> está listada.
    </li>
  </ul>

  <h3>🔄 Atualizando uma Imagem no Docker Hub</h3>
  <p>
    Para atualizar uma imagem já publicada no Docker Hub, você precisa reconstruir a imagem com as mudanças 
    desejadas e fazer o push novamente, seja com a mesma tag ou uma nova.
  </p>
  <ul>
    <li>
      <strong>Atualize o código ou Dockerfile:</strong><br>
      Faça as alterações necessárias no seu projeto ou no <code>Dockerfile</code> (ex.: atualizar dependências, 
      mudar configurações ou adicionar funcionalidades).
    </li>
    <li>
      <strong>Reconstrua a imagem:</strong><br>
      Execute o comando <code>docker build</code> com a mesma tag para sobrescrever a versão local ou uma nova 
      tag para versionamento:
      <pre><code>docker build -t seu-usuario/meu-app:1.0 .</code></pre>
      Ou, para uma nova versão:
      <pre><code>docker build -t seu-usuario/meu-app:1.1 .</code></pre>
    </li>
    <li>
      <strong>Faça o push da imagem atualizada:</strong><br>
      Após reconstruir, envie a imagem atualizada para o Docker Hub:
      <pre><code>docker push seu-usuario/meu-app:1.0</code></pre>
      Ou, para a nova versão:
      <pre><code>docker push seu-usuario/meu-app:1.1</code></pre>
      Se usar a mesma tag, a versão anterior no Docker Hub será sobrescrita. Se usar uma nova tag, ambas 
      as versões coexistirão no repositório.
    </li>
    <li>
      <strong>Gerencie versões no Docker Hub:</strong><br>
      Acesse <a href="https://hub.docker.com/" target="_blank">Docker Hub</a> para verificar todas as tags 
      disponíveis no seu repositório. Você pode manter várias versões (ex.: <code>1.0</code>, <code>1.1</code>, 
      <code>latest</code>) para diferentes casos de uso.
    </li>
  </ul>

  <h3>🏷️ Criando e Gerenciando Tags</h3>
  <p>
    Tags são usadas para versionar imagens e facilitar o gerenciamento de diferentes versões de uma mesma 
    aplicação. A tag <code>latest</code> é usada por padrão se nenhuma tag for especificada, mas é uma boa 
    prática criar tags específicas para cada versão.
  </p>
  <ul>
    <li>
      <strong>Criar uma nova tag:</strong><br>
      Para criar uma nova tag para uma imagem existente:
      <pre><code>docker tag seu-usuario/meu-app:1.0 seu-usuario/meu-app:1.1</code></pre>
      Isso cria uma nova tag (<code>1.1</code>) para a mesma imagem sem modificar a original.
    </li>
    <li>
      <strong>Adicionar a tag latest:</strong><br>
      Para marcar uma imagem como <code>latest</code>:
      <pre><code>docker tag seu-usuario/meu-app:1.1 seu-usuario/meu-app:latest</code></pre>
      Isso associa a tag <code>latest</code> à versão <code>1.1</code>. Quando usuários executarem 
      <code>docker pull seu-usuario/meu-app</code> sem especificar uma tag, a versão <code>latest</code> 
      será baixada.
    </li>
    <li>
      <strong>Publicar a nova tag:</strong><br>
      Após criar uma nova tag, faça o push para o Docker Hub:
      <pre><code>docker push seu-usuario/meu-app:1.1</code></pre>
      <pre><code>docker push seu-usuario/meu-app:latest</code></pre>
    </li>
    <li>
      <strong>Verificar tags locais:</strong><br>
      Liste todas as imagens e suas tags disponíveis localmente:
      <pre><code>docker images seu-usuario/meu-app</code></pre>
      Isso mostrará todas as tags associadas ao repositório <code>seu-usuario/meu-app</code>.
    </li>
  </ul>

  <h3>⬇️ Baixando Imagens do Docker Hub (Pull)</h3>
  <p>
    Para baixar sua própria imagem ou qualquer imagem pública do Docker Hub, use o comando 
    <code>docker pull</code>. Isso é útil para recuperar imagens que você publicou ou para usar imagens 
    de outros usuários.
  </p>
  <ul>
    <li>
      <strong>Baixe uma imagem específica:</strong><br>
      Para baixar uma imagem que você publicou, especificando a tag:
      <pre><code>docker pull seu-usuario/meu-app:1.0</code></pre>
      Se não especificar a tag, o Docker tentará baixar a tag <code>latest</code>:
      <pre><code>docker pull seu-usuario/meu-app</code></pre>
    </li>
    <li>
      <strong>Baixe uma imagem pública:</strong><br>
      Para baixar imagens públicas, como a imagem oficial do Node.js:
      <pre><code>docker pull node:18</code></pre>
    </li>
    <li>
      <strong>Verifique as imagens locais:</strong><br>
      Após o pull, liste as imagens disponíveis localmente:
      <pre><code>docker images</code></pre>
      Isso mostrará todas as imagens baixadas, incluindo <code>seu-usuario/meu-app:1.0</code> ou outras.
    </li>
  </ul>

  <h3>⚠️ Solucionando Problemas Comuns</h3>
  <ul>
    <li>
      <strong>Erro de autenticação:</strong><br>
      Se você encontrar um erro como <code>unauthorized: email must be verified</code>, verifique seu e-mail 
      no Docker Hub. Acesse <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>, faça login, e siga 
      as instruções para verificar seu e-mail. Depois, tente <code>docker login</code> novamente.
    </li>
    <li>
      <strong>Erro de permissão:</strong><br>
      Certifique-se de que o nome da imagem inclui seu nome de usuário do Docker Hub 
      (ex.: <code>seu-usuario/meu-app</code>). Você só pode fazer push para repositórios associados à sua conta.
    </li>
    <li>
      <strong>Limites de taxa (rate limits):</strong><br>
      O Docker Hub impõe limites para pulls anônimos e gratuitos. Se você atingir esses limites, faça login com 
      <code>docker login</code> para usar as cotas da sua conta verificada.
    </li>
    <li>
      <strong>Imagem não atualizada:</strong><br>
      Se a imagem baixada não reflete as alterações mais recentes, verifique se a tag correta foi usada. 
      Use <code>docker pull seu-usuario/meu-app:tag</code> com a tag específica ou assegure-se de que a tag 
      <code>latest</code> foi atualizada com <code>docker push</code>.
    </li>
  </ul>

  <h3>✅ Resumindo</h3>
  <ul>
    <li>Use <code>docker login</code> para autenticar-se no Docker Hub.</li>
    <li>Verifique seu e-mail no Docker Hub para evitar erros de autenticação.</li>
    <li>Use <code>docker build -t seu-usuario/nome-imagem:tag</code> ou <code>docker tag</code> para nomear imagens corretamente.</li>
    <li>Use <code>docker push seu-usuario/nome-imagem:tag</code> para publicar imagens no Docker Hub.</li>
    <li>Atualize imagens reconstruindo com <code>docker build</code> e fazendo push com a mesma ou nova tag.</li>
    <li>Crie tags específicas com <code>docker tag</code> para versionamento e publique-as com <code>docker push</code>.</li>
    <li>Use <code>docker pull seu-usuario/nome-imagem:tag</code> para baixar imagens do Docker Hub.</li>
    <li>Certifique-se de estar autenticado antes de fazer push ou pull de imagens privadas.</li>
  </ul>
</section>

<section id="docker-first-container">
  <h2>🐳 Rodando seu primeiro container Docker (2025)</h2>

  <p>
    O comando principal para rodar containers no Docker é:
  </p>
  <pre><code>docker run [opções] [imagem] [comando]</code></pre>
  <ul>
    <li><strong>[opções]</strong>: parâmetros adicionais como <code>--rm</code> ou <code>-it</code>.</li>
    <li><strong>[imagem]</strong>: a imagem Docker que você deseja usar (ex: <code>alpine</code>, <code>ubuntu</code>).</li>
    <li><strong>[comando]</strong>: o comando que será executado dentro do container.</li>
  </ul>
  <p>
    Exemplo simples:
  </p>
  <pre><code>docker run --rm alpine echo "Hello Docker!"</code></pre>

  <h3>1️⃣ Teste básico com Alpine</h3>
  <p>Alpine é uma imagem Linux mínima, muito leve e rápida:</p>
  <pre><code>docker run --rm alpine echo "Hello Docker!"</code></pre>
  <ul>
    <li><strong>--rm</strong>: remove o container assim que terminar.</li>
    <li><strong>echo "Hello Docker!"</strong>: imprime a mensagem dentro do container.</li>
    <li>Se a imagem Alpine não estiver no seu computador, o Docker fará download automaticamente.</li>
  </ul>

  <h3>2️⃣ Teste com Debian ou Ubuntu</h3>
  <p>Você também pode usar imagens maiores, com mais recursos:</p>
  <pre><code>docker run --rm debian echo "Hello Docker!"</code></pre>
  <pre><code>docker run --rm ubuntu echo "Hello Docker!"</code></pre>

  <h3>3️⃣ Rodando um container interativo</h3>
  <p>Para abrir um terminal dentro do container e testar Linux:</p>
  <pre><code>docker run --rm -it ubuntu bash</code></pre>
  <ul>
    <li><strong>-it</strong>: abre o container em modo interativo com terminal.</li>
    <li>Dentro do shell do container, você pode rodar Linux normalmente.</li>
    <li>Digite <code>exit</code> para sair do container.</li>
  </ul>

  <h3>✅ Resumo</h3>
  <ul>
    <li>O comando base é <code>docker run [opções] [imagem] [comando]</code></li>
    <li>Use <code>--rm</code> para containers temporários</li>
    <li>Use <code>-it</code> se quiser interagir com o container</li>
    <li>Docker Desktop no Windows já inclui tudo que você precisa para rodar containers</li>
  </ul>
</section>

<section id="docker-imagem-container">
  <h2>📦 Imagem vs 🐳 Container no Docker</h2>

  <h3>O que é uma Imagem Docker?</h3>
  <p>
    Uma <strong>Imagem</strong> é como uma <em>fotografia (snapshot)</em> ou uma 
    <em>receita de bolo</em>. Ela contém tudo o que é necessário para executar um software:
  </p>
  <ul>
    <li>Sistema operacional base (ex: Debian, Alpine, Ubuntu)</li>
    <li>Dependências (bibliotecas, pacotes, frameworks)</li>
    <li>Código do aplicativo</li>
    <li>Configurações padrão</li>
  </ul>
  <p>
    Características principais:
  </p>
  <ul>
    <li>É <strong>imutável</strong> (não muda após ser criada).</li>
    <li>Pode ser distribuída pelo <strong>Docker Hub</strong> ou registries privados.</li>
    <li>É <strong>reutilizável</strong>: várias pessoas podem rodar a mesma imagem.</li>
  </ul>
  <pre><code>docker pull ubuntu</code></pre>
  <p>Esse comando baixa a imagem do Ubuntu, mas ela ainda não está em execução.</p>

  <h3>O que é um Container Docker?</h3>
  <p>
    Um <strong>Container</strong> é uma <em>instância em execução</em> de uma imagem. 
    Usando a analogia do bolo: a imagem é a receita, o container é o bolo pronto na mesa.
  </p>
  <ul>
    <li>É criado a partir de uma imagem.</li>
    <li>É <strong>isolado</strong> (tem seu próprio sistema de arquivos, processos e rede).</li>
    <li>É <strong>descartável</strong>: pode ser parado e removido sem afetar a imagem.</li>
    <li>Pode ser <strong>reproduzido</strong> em qualquer máquina que tenha Docker.</li>
  </ul>
  <pre><code>docker run --rm ubuntu echo "Hello Docker!"</code></pre>
  <p>
    Neste exemplo, o Docker cria um container temporário usando a imagem <code>ubuntu</code>, 
    executa o comando e depois remove o container.
  </p>

  <h3>🔑 Diferença resumida</h3>
  <table border="1" cellspacing="0" cellpadding="6">
    <thead>
      <tr>
        <th>Conceito</th>
        <th>Analogia</th>
        <th>Explicação simples</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Imagem</strong></td>
        <td>📜 Receita de bolo</td>
        <td>Conjunto de instruções e ingredientes (SO, libs, app)</td>
      </tr>
      <tr>
        <td><strong>Container</strong></td>
        <td>🍰 Bolo pronto</td>
        <td>Execução real da receita (instância da imagem)</td>
      </tr>
    </tbody>
  </table>
</section>

<section id="docker-images-and-commands">
  <h2>📦 Imagens Docker</h2>

  <h3>🔎 Onde encontrar imagens?</h3>
  <p>
    As imagens oficiais do Docker podem ser encontradas no 
    <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>, 
    que funciona como um repositório central de imagens prontas para uso.
  </p>
  <ul>
    <li>🔹 <code>alpine</code>: Imagem mínima baseada em Linux, super leve.</li>
    <li>🔹 <code>ubuntu</code>: Imagem oficial do Ubuntu.</li>
    <li>🔹 <code>debian</code>: Imagem oficial do Debian.</li>
    <li>🔹 <code>nginx</code>: Servidor web popular.</li>
    <li>🔹 <code>mysql</code> ou <code>postgres</code>: Bancos de dados relacionais.</li>
  </ul>
</section>

<section id="docker-basic-commands">
  <h2>⚙️ Comandos Docker Gerais</h2>

  <h3>⚙️ Comandos básicos</h3>
  <p>Aqui estão alguns comandos essenciais para começar:</p>
  <ul>
    <li>
      <pre><code>docker run --rm -it --name meu_container ubuntu bash</code></pre>
      <strong>-i</strong>: Mantém o modo interativo ativo (stdin aberto).<br>
      <strong>-t</strong>: Aloca um terminal (tty) para o container.<br>
      <strong>-it</strong>: Combina os dois, permitindo interação total com o container.<br>
      <strong>--name meu_container</strong>: dá um nome específico para o container.<br>
      <strong>--rm</strong>: remove o container automaticamente após parar.
    </li>
    <li>
      <pre><code>exit</code></pre>
      Sai de um container interativo.
    </li>
    <li>
      <pre><code>docker ps</code></pre>
      Lista os containers em execução.
    </li>
    <li>
      <pre><code>docker ps -a</code></pre>
      Lista todos os containers, incluindo os parados.
    </li>
    <li>
      <pre><code>docker stop [nome_ou_id]</code></pre>
      Para um container em execução.
    </li>
    <li>
      <pre><code>docker start -i [nome_ou_id]</code></pre>
      Reinicia um container parado em modo interativo.
    </li>
    <li>
      <pre><code>docker rm [nome_ou_id]</code></pre>
      Remove um container parado do sistema.
    </li>
    <li>
      <pre><code>docker rm -f [nome_ou_id]</code></pre>
      Força a remoção de um container em execução.
    </li>
    <li>
      <pre><code>docker run -d --name meu_container ubuntu</code></pre>
      Roda o container em background (<strong>-d</strong> = detached) e dá um nome.
    </li>
    <li>
      <pre><code>docker logs [nome_ou_id]</code></pre>
      Mostra os logs de saída de um container em execução ou parado.
    </li>
    <li>
      <pre><code>docker logs -f [nome_ou_id]</code></pre>
      Mostra os logs em tempo real (<strong>-f</strong> = follow).
    </li>
    <li>
      <pre><code>docker logs --tail 50 [nome_ou_id]</code></pre>
      Mostra apenas as últimas 50 linhas de log.
    </li>
    <li>
      <pre><code>docker images</code></pre>
      Lista todas as imagens disponíveis localmente.
    </li>
    <li>
      <pre><code>docker rmi [imagem]</code></pre>
      Remove uma imagem do sistema (precisa que nenhum container esteja usando ela).
    </li>
    <li>
      <pre><code>docker rmi -f [imagem]</code></pre>
      Força a remoção de uma imagem mesmo que esteja em uso por containers.
    </li>
    <li>
      <pre><code>docker system prune</code></pre>
      Remove <strong>todos os recursos não utilizados</strong> (containers parados, redes órfãs, volumes anônimos e imagens dangling).  
      ⚠️ Use com cuidado: pode apagar mais do que você espera.
    </li>
    <li>
      <pre><code>docker cp [nome_ou_id]:/caminho/no/container /caminho/no/host</code></pre>
      Copia arquivos ou diretórios de um container para o host.<br>
      Exemplo: Copiar uma imagem de um container para o host:
      <pre><code>docker cp meu_container:/app/imagem.jpg /home/user/imagens/</code></pre>
    </li>
    <li>
      <pre><code>docker cp /caminho/no/host [nome_ou_id]:/caminho/no/container</code></pre>
      Copia arquivos ou diretórios do host para um container.<br>
      Exemplo: Copiar uma imagem do host para um container:
      <pre><code>docker cp /home/user/imagens/imagem.jpg meu_container:/app/</code></pre>
    </li>
    <li>
      <pre><code>docker top [nome_ou_id]</code></pre>
      Exibe os processos em execução dentro de um container.<br>
      Exemplo: Ver os processos ativos de um container chamado <code>meu_container</code>:<br>
      <pre><code>docker top meu_container</code></pre>
      Este comando mostra uma tabela com informações como PID, usuário, comando em execução e uso de recursos, semelhante ao comando <code>top</code> no Linux.
    </li>
    <li>
      <pre><code>docker inspect [nome_ou_id]</code></pre>
      Exibe informações detalhadas sobre um container ou imagem em formato JSON.<br>
      Exemplo: Inspecionar os detalhes de um container chamado <code>meu_container</code>:<br>
      <pre><code>docker inspect meu_container</code></pre>
      Este comando retorna informações como configuração, estado, rede, volumes e variáveis de ambiente do container. Útil para depuração ou para verificar detalhes como portas mapeadas ou configurações de montagem.
    </li>
    <li>
      <pre><code>docker stats [nome_ou_id]</code></pre>
      Exibe estatísticas de uso de recursos de um ou mais containers em tempo real.<br>
      Exemplo: Ver o uso de CPU, memória e rede de um container chamado <code>meu_container</code>:<br>
      <pre><code>docker stats meu_container</code></pre>
      Este comando mostra uma tabela com informações como uso de CPU (%), memória (usada/limite), tráfego de rede e I/O de disco. Para monitorar todos os containers em execução, use <code>docker stats</code> sem especificar um nome ou ID. Pressione <code>Ctrl+C</code> para sair do modo de monitoramento.
    </li>
  </ul>

  <h3>✅ Resumindo</h3>
  <ul>
    <li>Procure imagens no <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>.</li>
    <li>Use <code>docker run</code> para executar containers.</li>
    <li>Use <code>-i</code> e <code>-t</code> para interação.</li>
    <li>Use <code>-d</code> para rodar containers em background.</li>
    <li>Use <code>--name [nome]</code> para dar nomes aos containers.</li>
    <li>Use <code>--rm</code> para remover automaticamente containers temporários.</li>
    <li>Use <code>docker start -i [nome_ou_id]</code> para reabrir containers parados.</li>
    <li>Use <code>docker stop [nome_ou_id]</code> para parar containers.</li>
    <li>Use <code>docker rm [nome_ou_id]</code> para remover containers parados.</li>
    <li>Use <code>docker rm -f [nome_ou_id]</code> para forçar a remoção de containers.</li>
    <li>Use <code>docker rmi [imagem]</code> para remover imagens não usadas.</li>
    <li>Use <code>docker rmi -f [imagem]</code> para forçar a remoção de imagens.</li>
    <li>Use <code>docker system prune</code> para limpar recursos não utilizados.</li>
    <li>Use <code>docker logs [nome_ou_id]</code> para ver logs.</li>
    <li>Use <code>docker cp</code> para copiar arquivos entre o host e containers.</li>
    <li>Use <code>docker top [nome_ou_id]</code> para visualizar os processos em execução em um container.</li>
    <li>Use <code>docker inspect [nome_ou_id]</code> para obter informações detalhadas sobre containers ou imagens.</li>
    <li>Use <code>docker stats [nome_ou_id]</code> para monitorar o uso de recursos de containers em tempo real.</li>
    <li>Com <code>docker ps</code> e <code>docker images</code> você monitora containers e imagens.</li>
  </ul>
</section>

<section id="container-vs-vm">
  <h2>⚖️ Containers vs Máquinas Virtuais (VMs)</h2>

  <p>
    Containers e Máquinas Virtuais (VMs) são tecnologias que permitem executar aplicativos isolados, 
    mas funcionam de formas diferentes. Entender a diferença é essencial para escolher a abordagem certa.
  </p>

  <h3>1️⃣ Máquinas Virtuais (VMs)</h3>
  <p>
    Uma VM emula um computador completo, incluindo kernel, sistema operacional e hardware virtual. 
    Cada VM roda sobre um hypervisor (como VMware, VirtualBox ou Hyper-V).
  </p>
  <ul>
    <li><strong>Vantagens:</strong>
      <ul>
        <li>Isolamento completo: cada VM tem seu próprio SO, evitando conflitos.</li>
        <li>Compatibilidade: qualquer software que roda no SO convidado funciona na VM.</li>
        <li>Segurança: falhas em uma VM dificilmente afetam outras VMs ou o host.</li>
      </ul>
    </li>
    <li><strong>Desvantagens:</strong>
      <ul>
        <li>Mais pesado: cada VM precisa de seu próprio SO, consumindo mais RAM e CPU.</li>
        <li>Demora para iniciar: boot completo do sistema operacional.</li>
        <li>Menos portátil: mover VMs entre hosts é mais lento e complexo.</li>
      </ul>
    </li>
    <li><strong>Cenários de uso:</strong>
      <ul>
        <li>Executar diferentes sistemas operacionais em um único servidor (ex: Windows e Linux).</li>
        <li>Ambientes que precisam de isolamento extremo.</li>
        <li>Testes de software em múltiplas versões de SO.</li>
      </ul>
    </li>
  </ul>

  <h3>2️⃣ Containers</h3>
  <p>
    Containers compartilham o kernel do sistema host e isolam apenas o ambiente de execução do aplicativo. 
    Eles são leves, rápidos e portáteis.
  </p>
  <ul>
    <li><strong>Vantagens:</strong>
      <ul>
        <li>Leveza: containers compartilham recursos do SO, usando menos RAM e CPU.</li>
        <li>Portabilidade: a mesma imagem funciona em qualquer host com Docker.</li>
        <li>Inicialização rápida: start em segundos.</li>
        <li>Escalabilidade: fácil replicação de múltiplos containers.</li>
      </ul>
    </li>
    <li><strong>Desvantagens:</strong>
      <ul>
        <li>Isolamento menor: compartilham kernel, vulnerabilidades do host podem afetar containers.</li>
        <li>Dependência do SO host: containers Linux não rodam nativamente em Windows e vice-versa.</li>
        <li>Compatibilidade limitada: aplicativos que exigem kernel diferente podem não funcionar.</li>
      </ul>
    </li>
    <li><strong>Cenários de uso:</strong>
      <ul>
        <li>Deploy rápido de aplicações em produção.</li>
        <li>Microservices: cada serviço em um container isolado.</li>
        <li>Ambientes de desenvolvimento consistentes entre máquinas.</li>
        <li>Testes rápidos e automação de pipelines CI/CD.</li>
      </ul>
    </li>
  </ul>

  <h3>3️⃣ Comparativo resumido</h3>
  <table border="1" cellspacing="0" cellpadding="6">
    <thead>
      <tr>
        <th>Aspecto</th>
        <th>Máquinas Virtuais (VMs)</th>
        <th>Containers</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Isolamento</td>
        <td>Completo, cada VM tem seu SO</td>
        <td>Parcial, compartilha kernel do host</td>
      </tr>
      <tr>
        <td>Leveza</td>
        <td>Pesado, cada VM tem SO completo</td>
        <td>Leve, compartilha kernel e recursos</td>
      </tr>
      <tr>
        <td>Portabilidade</td>
        <td>Moderada, imagens de VM grandes</td>
        <td>Alta, imagens pequenas e replicáveis</td>
      </tr>
      <tr>
        <td>Tempo de inicialização</td>
        <td>Minutos</td>
        <td>Segundos</td>
      </tr>
      <tr>
        <td>Cenários ideais</td>
        <td>Testes de SO, isolamento extremo</td>
        <td>Deploy rápido, microservices, CI/CD</td>
      </tr>
    </tbody>
  </table>
</section>

<section id="exposing-ports">
  <h2>🌐 Expondo portas no container</h2>
  <p>
    Por padrão, os containers do Docker rodam isolados do seu host. Para acessar um serviço rodando dentro do container (como o <code>nginx</code>), é necessário mapear as portas do container para portas do host usando o parâmetro <code>-p</code>.
  </p>

  <ul>
    <li>
      <pre><code>docker run -d -p 80:80 nginx</code></pre>
      Executa o <strong>nginx</strong> em segundo plano, mapeando a porta <code>80</code> do host para a porta <code>80</code> do container.
    </li>
    <li>
      <pre><code>docker ps</code></pre>
      Mostra os containers rodando e quais portas estão expostas:
      <br>
      <code>0.0.0.0:80->80/tcp</code> significa que você pode acessar no navegador <a href="http://localhost:80" target="_blank">http://localhost</a>.
    </li>
    <li>
      <pre><code>docker run --rm -d -p 3000:80 nginx</code></pre>
      Executa o nginx mapeando a porta <code>3000</code> do host para a porta <code>80</code> do container.  
      Agora você acessa em <a href="http://localhost:3000" target="_blank">http://localhost:3000</a>.
    </li>
    <li>
      <pre><code>docker stop [nome_ou_id]</code></pre>
      Para o container rodando na porta exposta.
    </li>
  </ul>

  <h3>✅ Resumindo</h3>
  <ul>
    <li>Use <code>-p [porta_host]:[porta_container]</code> para expor serviços.</li>
    <li>Se não especificar, o container fica isolado (não acessível externamente).</li>
    <li>Você pode rodar o mesmo serviço em várias portas diferentes do host, mudando apenas o primeiro número (exemplo: <code>-p 3000:80</code>, <code>-p 4000:80</code>).</li>
  </ul>
</section>

<section id="criando-imagens-docker">
  <h2>🛠️ Criando sua própria Imagem Docker</h2>

  <p>
    Além de usar imagens já prontas do <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>, 
    você também pode <strong>criar suas próprias imagens</strong>.  
    Para isso usamos um arquivo chamado <code>Dockerfile</code>, que contém as instruções
    necessárias para montar a imagem.
  </p>

  <h3>📄 Exemplo de Dockerfile</h3>
  <pre><code>FROM node
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]</code></pre>

  <ul>
    <li><strong>FROM node</strong>: usa a imagem oficial do Node como base.</li>
    <li><strong>WORKDIR /app</strong>: define a pasta de trabalho no container.</li>
    <li><strong>COPY package*.json ./</strong>: copia os arquivos de dependências.</li>
    <li><strong>RUN npm install</strong>: instala as dependências.</li>
    <li><strong>COPY . .</strong>: copia o restante do código para o container.</li>
    <li><strong>EXPOSE 3000</strong>: expõe a porta que o app vai rodar.</li>
    <li><strong>CMD ["node", "app.js"]</strong>: comando que inicia o servidor.</li>
  </ul>

  <h3>⬇️ Baixando Imagens do Docker Hub</h3>
  <p>
    Antes de criar suas próprias imagens, você pode <strong>baixar imagens prontas</strong> do Docker Hub 
    usando o comando <code>docker pull</code>.  
    Por exemplo, para baixar a imagem oficial do Node:
  </p>
  <pre><code>docker pull node</code></pre>
  <p>
    Isso garante que você tenha a versão mais atualizada da imagem localmente.  
    Você também pode especificar uma versão específica:
  </p>
  <pre><code>docker pull node:18</code></pre>
  <ul>
    <li><strong>node</strong>: baixa a última versão disponível da imagem Node.js.</li>
    <li><strong>node:18</strong>: baixa especificamente a versão 18 do Node.js.</li>
  </ul>

  <h3>📦 Criando a Imagem</h3>
  <p>
    Para criar a imagem a partir do <code>Dockerfile</code>, use o comando:
  </p>
  <pre><code>docker build -t meu-app-node .</code></pre>
  <ul>
    <li><strong>-t meu-app-node</strong>: dá o nome <em>meu-app-node</em> para a imagem.</li>
    <li><strong>.</strong>: indica que o <code>Dockerfile</code> está no diretório atual.</li>
  </ul>

  <h3>🔄 Atualizando a Imagem</h3>
  <p>
    Sempre que você alterar o código do seu projeto ou o <code>Dockerfile</code>, 
    é necessário reconstruir a imagem para que as mudanças entrem em efeito:
  </p>
  <pre><code>docker build -t meu-app-node .</code></pre>
  <p>
    Se quiser substituir a imagem antiga, basta usar o mesmo nome.  
    Depois, reinicie o container para rodar a nova versão:
  </p>
  <pre><code>docker stop meu-container-node
docker rm meu-container-node
docker run -d -p 3000:3000 --name meu-container-node meu-app-node</code></pre>
  <ul>
    <li><strong>docker stop</strong>: para o container em execução.</li>
    <li><strong>docker rm</strong>: remove o container antigo.</li>
    <li><strong>docker run</strong>: cria e inicia um novo container com a imagem atualizada.</li>
  </ul>

  <h3>⚡ Cache das Imagens</h3>
  <p>
    O Docker utiliza <strong>camadas de cache</strong> para acelerar o processo de build.  
    Isso significa que, se nada mudou em uma instrução do <code>Dockerfile</code>, 
    a camada correspondente não será reconstruída.
  </p>
  <p>
    Para forçar a reconstrução sem usar o cache, utilize:
  </p>
  <pre><code>docker build --no-cache -t meu-app-node .</code></pre>
  <p>
    Isso garante que todas as etapas sejam executadas novamente, útil quando você suspeita
    que alguma dependência ou configuração antiga ainda está sendo usada.
  </p>

  <h3>🐳 Rodando o Container</h3>
  <p>
    Depois que a imagem for criada ou atualizada, você pode rodar um container com:
  </p>
  <pre><code>docker run -d -p 3000:3000 --name meu-container-node meu-app-node</code></pre>
  <ul>
    <li><strong>-d</strong>: executa em segundo plano (detached).</li>
    <li><strong>-p 3000:3000</strong>: mapeia a porta <code>3000</code> do host para a porta <code>3000</code> do container.</li>
    <li><strong>--name meu-container-node</strong>: dá um nome ao container.</li>
    <li><strong>meu-app-node</strong>: é a imagem criada anteriormente.</li>
  </ul>

  <h3>🌐 Acessando o App</h3>
  <p>
    Agora basta abrir no navegador:
  </p>
  <pre><code>http://localhost:3000</code></pre>
  <p>
    Você verá a mensagem <strong>Hello World!</strong> do seu servidor Node.js rodando dentro do container 🚀
  </p>

  <h3>📂 Rodando Múltiplas Aplicações no Mesmo Container</h3>
  <p>
    Embora a prática recomendada seja <strong>um processo por container</strong>, tecnicamente é possível rodar várias aplicações no mesmo container.  
    Por exemplo, você pode rodar dois servidores Node.js em portas diferentes:
  </p>
  <pre><code>// app1.js
const express = require("express");
const app1 = express();
app1.get("/", (req, res) => res.send("App 1 rodando na porta 3000"));
app1.listen(3000);

// app2.js
const express = require("express");
const app2 = express();
app2.get("/", (req, res) => res.send("App 2 rodando na porta 4000"));
app2.listen(4000);</code></pre>

  <p>
    E no <code>Dockerfile</code>, você poderia rodar os dois usando um gerenciador de processos como o <strong>PM2</strong> or using a custom script:
  </p>
  <pre><code>CMD ["sh", "-c", "node app1.js & node app2.js && wait"]</code></pre>

  <p>
    Assim, o mesmo container pode responder em múltiplas portas (ex.: 3000 e 4000).  
    No entanto, em ambientes de produção o ideal é separar cada aplicação em seu próprio container e usar o Docker Compose para orquestrá-los.
  </p>

  <h3>🏷️ Renomeando Imagens e Adicionando Tags</h3>
  <p>
    No Docker, toda imagem pode ter um <strong>nome</strong> e uma <strong>tag</strong> 
    (por padrão, a tag é <code>latest</code> se não for especificada).  
    Você pode renomear ou criar novas tags para uma imagem existente com o comando:
  </p>
  <pre><code>docker tag meu-app-node meu-usuario/meu-app:1.0</code></pre>
  <ul>
    <li><strong>meu-app-node</strong>: nome da imagem local que já existe.</li>
    <li><strong>meu-usuario/meu-app</strong>: novo nome da imagem (geralmente usado para push no Docker Hub).</li>
    <li><strong>:1.0</strong>: tag personalizada (exemplo: versão 1.0).</li>
  </ul>

  <p>
    Também é possível <strong>renomear no momento do build</strong>, atribuindo nome e tag diretamente:
  </p>
  <pre><code>docker build -t meu-usuario/meu-app:2.0 .</code></pre>
  <ul>
    <li><strong>-t</strong>: define o nome e a tag da imagem já no build.</li>
    <li><strong>meu-usuario/meu-app:2.0</strong>: nome e tag desejados.</li>
    <li><strong>.</strong>: diretório onde está o <code>Dockerfile</code>.</li>
  </ul>

  <p>
    Para listar todas as imagens disponíveis localmente, use:
  </p>
  <pre><code>docker images</code></pre>

  <p>
    Caso queira remover uma imagem antiga ou com tag errada:
  </p>
  <pre><code>docker rmi meu-usuario/meu-app:1.0</code></pre>

  <p>
    ➡️ Essa prática é muito útil quando você quer versionar suas imagens,  
    manter múltiplas versões do mesmo projeto ou publicar no <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>.
  </p>

  <h3>✅ Resumindo</h3>
  <ul>
    <li>Use <code>docker pull nome-imagem</code> para baixar imagens prontas do Docker Hub.</li>
    <li>Escreva um <code>Dockerfile</code> com as instruções da sua aplicação.</li>
    <li>Use <code>docker build -t nome-imagem .</code> para criar ou atualizar a imagem.</li>
    <li>Use <code>docker build --no-cache</code> quando quiser reconstruir tudo do zero.</li>
    <li>Use <code>docker run -p porta:porta nome-imagem</code> para rodar um container.</li>
    <li>Você pode rodar múltiplas aplicações no mesmo container, mas em produção prefira separar em containers diferentes.</li>
  </ul>
</section>

<h2>💾 O que são Volumes no Docker?</h2>

<p>
  Os <strong>Volumes</strong> são o recurso do Docker para garantir <strong>persistência de dados</strong>. 
  Containers são, por natureza, <em>temporários</em>: se você parar e remover um container, todos os dados gravados dentro dele 
  (arquivos, logs, banco de dados, uploads) são perdidos. Com volumes, esses dados podem ser armazenados fora do ciclo de vida do container, 
  de forma independente e reutilizável.
</p>

<p>
  Em resumo, os volumes permitem que você:
</p>

<ul>
  <li>Mantenha dados salvos mesmo após a exclusão de um container.</li>
  <li>Compartilhe informações entre múltiplos containers.</li>
  <li>Tenha desempenho superior ao sistema de arquivos do container.</li>
  <li>Faça backup ou restauração de dados de maneira simples.</li>
</ul>

<p>
  <strong>Exemplo prático:</strong> neste repositório, criamos uma aplicação PHP simples que salva mensagens enviadas por formulário.  
  Sem volumes, os arquivos de mensagens (<code>msg-0.txt</code>, <code>msg-1.txt</code>, etc.) seriam perdidos ao remover o container.  
  Com volumes, eles ficam salvos e podem ser acessados em <code>http://localhost/messages/</code> mesmo depois de reiniciar ou recriar o container.
</p>

<pre><code># Executando o container com bind mount (linkando a pasta "messages" ao host)
docker run -d -p 80:80 -v $(pwd)/messages:/var/www/html/messages meu-php-app
</code></pre>

<p>
  Agora, cada mensagem enviada será salva na pasta <code>messages</code> do host e persistirá, mesmo que o container seja removido.  
</p>


<h2>🗂️ Tipos de Volumes no Docker</h2>

<p>O Docker trabalha basicamente com três tipos de volumes. Cada um tem seu uso e importância:</p>

<h3>1. Volumes Nomeados</h3>
<ul>
  <li>São volumes <strong>criando com um nome definido pelo usuário</strong>, o que facilita identificar e reutilizar depois.</li>
  <li>Gerenciados pelo Docker e armazenados em <code>/var/lib/docker/volumes/</code> no host.</li>
  <li>Ideais para produção, porque você controla melhor o ciclo de vida e pode reaproveitar facilmente.</li>
  <li>Exemplo:
    <pre><code>docker run -d -v meu-volume:/var/lib/mysql mysql:8</code></pre>
    Aqui, o volume <code>meu-volume</code> vai persistir os dados do MySQL.
  </li>
</ul>

<h3>2. Volumes Anônimos</h3>
<ul>
  <li>O Docker cria automaticamente quando você usa <code>-v /caminho/no/container</code> sem especificar nome.</li>
  <li>São úteis para testes rápidos, mas <strong>difíceis de gerenciar</strong>, já que recebem um nome aleatório.</li>
  <li>Podem acumular e ocupar espaço no host se não forem limpos.</li>
  <li>Exemplo:
    <pre><code>docker run -d -v /var/lib/mysql mysql:8</code></pre>
    O Docker cria um volume anônimo para mapear <code>/var/lib/mysql</code>.
  </li>
</ul>

<h3>3. Bind Mounts</h3>
<ul>
  <li>Mapeiam diretamente uma pasta ou arquivo do host para dentro do container.</li>
  <li>Úteis em <strong>desenvolvimento</strong>, porque as alterações feitas no host refletem no container em tempo real.</li>
  <li>Dependem do caminho absoluto do host → menos portáveis para produção.</li>
  <li>Exemplo prático com este projeto:
    <pre><code>docker run -d -p 80:80 -v $(pwd)/messages:/var/www/html/messages meu-php-app</code></pre>
    Assim, a pasta <code>./messages</code> do host fica sincronizada com <code>/var/www/html/messages</code> no container, 
    garantindo que os arquivos de mensagens não se percam.
  </li>
</ul>

<h3>⚙️ Comandos úteis para Volumes</h3>
<ul>
  <li><code>docker volume ls</code> → lista volumes existentes.</li>
  <li><code>docker volume inspect meu-volume</code> → mostra detalhes de um volume.</li>
  <li><code>docker volume rm meu-volume</code> → remove um volume não utilizado.</li>
  <li><code>docker volume prune</code> → apaga volumes órfãos (cuidado: pode apagar dados importantes).</li>
</ul>

<h3>✅ Boas práticas</h3>
<ul>
  <li>Prefira volumes gerenciados em produção.</li>
  <li>Use bind mounts em desenvolvimento (facilitam alterações no código).</li>
  <li>Nomeie volumes de forma clara (<code>mysql-data</code>, <code>logs-app</code>, etc.).</li>
  <li>Faça backup dos volumes regularmente.</li>
</ul>

<h2>🛠️ Criando Volumes Manualmente</h2>

<p>
  Embora o Docker crie volumes automaticamente quando você usa <code>-v</code> sem especificar nada, é uma boa prática 
  <strong>criar volumes manualmente</strong> e dar nomes claros para facilitar o gerenciamento, backup e reutilização.
</p>

<ul>
  <li>
    <h3>Criando um volume</h3>
    <pre><code>docker volume create meu-volume</code></pre>
    <p>
      Esse comando cria um volume chamado <code>meu-volume</code>, que fica armazenado no host (normalmente em 
      <code>/var/lib/docker/volumes/meu-volume/</code> no Linux).
    </p>
  </li>

  <li>
    <h3>Usando o volume em um container</h3>
    <pre><code>docker run -d -v meu-volume:/app/dados meu-container</code></pre>
    <ul>
      <li><code>meu-volume</code> → nome do volume no host (criado manualmente).</li>
      <li><code>/app/dados</code> → diretório dentro do container onde o volume será montado.</li>
    </ul>
  </li>

  <li>
    <h3>Usando o volume em modo somente leitura</h3>
    <pre><code>docker run -d -v meu-volume:/app/dados:ro meu-container</code></pre>
    <p>
      O sufixo <code>:ro</code> (<em>read-only</em>) garante que o container só possa <strong>ler</strong> os dados do volume, 
      sem modificar nada. Útil em casos onde os dados devem ser consumidos mas nunca alterados, como arquivos de configuração ou datasets fixos.
    </p>
  </li>

  <li>
    <h3>Inspecionando volumes</h3>
    <pre><code>docker volume inspect meu-volume</code></pre>
    <p>
      Mostra detalhes sobre onde o volume está armazenado, quais containers estão usando e outras informações úteis.
    </p>
  </li>

  <li>
    <h3>Listando volumes</h3>
    <pre><code>docker volume ls</code></pre>
  </li>

  <li>
    <h3>Removendo volumes</h3>
    <pre><code>docker volume rm meu-volume</code></pre>
    <p>
      Remove o volume (desde que nenhum container esteja usando).  
      Para remover todos os volumes não utilizados:
    </p>
    <pre><code>docker volume prune</code></pre>
    <p><strong>⚠️ Atenção:</strong> esse comando pode apagar dados importantes se usado sem cuidado.</p>
  </li>
</ul>

<h2>🌐 Conectando Containers com Networks no Docker</h2>

<p>
  No Docker, <strong>networks</strong> definem como os containers se comunicam entre si e (opcionalmente) com o mundo externo.
  Elas oferecem isolamento, resolução de nomes (<em>DNS</em> interno), sub-redes e regras de comunicação previsíveis.
  Em vez de ligar containers por IP (que muda), você usa <strong>nomes de serviço</strong> ou <strong>aliases</strong>.
</p>

<h3>🔑 Conceitos-chave</h3>
<ul>
  <li><strong>Isolamento:</strong> cada network é um domínio de broadcast separado; containers só se veem se estiverem na mesma network.</li>
  <li><strong>DNS interno:</strong> o Docker resolve automaticamente o nome do container para o IP dentro da network.</li>
  <li><strong>Portas:</strong> expor/publicar portas (<code>-p</code>) é para acesso <em>externo</em>; entre containers na mesma network não é necessário mapear portas.</li>
</ul>

<pre>
Host ──(porta 8080 mapeada)──► Container web:80
          ▲
          │ (não precisa mapear portas entre containers)
          └───────► Container db:3306 (mesma network, acesso por nome "db")
</pre>

<hr/>

<h2>🧭 Tipos de Network</h2>

<h3>1) bridge (padrão)</h3>
<p>
  Rede local criada no host (NAT). Boa para desenvolvimento e cenários single-host.
  Containers se comunicam entre si pelo nome dentro da mesma bridge.
</p>

<h3>2) host</h3>
<p>
  O container compartilha a pilha de rede do host (sem isolamento de portas). Útil para serviços que precisam de performance
  de rede máxima ou descoberta de multicast/UDP sem NAT. Só Linux.
</p>

<h3>3) none</h3>
<p>
  Sem rede (isolamento total). Útil para <em>jobs</em> offline, processamento batch, ou segurança extra.
</p>

<h3>4) overlay (Swarm/K8s)</h3>
<p>
  Rede distribuída que conecta containers em múltiplos hosts (cluster). Requer Docker Swarm/Kubernetes.
</p>

<h3>5) macvlan</h3>
<p>
  Atribui um MAC próprio ao container e o liga diretamente à rede física (parece um dispositivo na LAN). Útil para
  integrar com infra já existente que exige IPs “reais”.
</p>

<hr/>

<h2>🛠️ Criando e Conectando Containers (bridge)</h2>

<h3>1) Criar uma network</h3>
<pre><code>docker network create --driver bridge minha-net</code></pre>

<h3>2) Rodar containers já conectados</h3>
<pre><code>docker run -d --name db --network minha-net -e MYSQL_ROOT_PASSWORD=senha mysql:8
docker run -d --name web --network minha-net -p 8080:80 meu-web:latest</code></pre>
<p>
  Agora o container <code>web</code> acessa o banco usando <code>db:3306</code> (por nome!). Do host, acesse o web em <code>http://localhost:8080</code>.
</p>

<h3>3) Conectar/Desconectar depois de rodar</h3>
<pre><code>docker network connect minha-net web
docker network disconnect minha-net web</code></pre>

<h3>4) Ver redes e detalhes</h3>
<pre><code>docker network ls
docker network inspect minha-net</code></pre>

<h3>5) Remover uma network</h3>
<pre><code>docker network rm minha-net</code></pre>
<p>
  Remove a rede <code>minha-net</code>. Atenção: não pode haver containers em uso nessa rede.
</p>

<h3>6) Remover todas as networks não utilizadas</h3>
<pre><code>docker network prune</code></pre>
<p>
  Remove todas as redes que não têm containers conectados. Será exibida uma mensagem de confirmação antes da exclusão.
</p>

<hr/>

<h2>🏗️ Arquitetura de Containers Flask com Conexão Externa</h2>

<h3>🌐 1. Container Externo (flaskexterna)</h3>
<p>
  Este container executa um serviço Flask que funciona como uma API externa. Ele é responsável por fornecer dados de usuários aleatórios através da API <a href="https://randomuser.me/api" target="_blank">randomuser.me</a>.
</p>
<ul>
  <li> Base: Python 3</li>
  <li> Dependências: Flask, requests</li>
  <li> Porta exposta: 5000</li>
  <li> Arquivo principal: <code>app.py</code></li>
  <li> Funcionalidade: Retorna JSON com dados de usuários ao acessar a rota <code>/</code></li>
</ul>

<h3>🏠 2. Container Host (flaskhost)</h3>
<p>
  Este container executa um serviço Flask que atua como “host” e se conecta ao container externo para consumir dados, além de integrar com banco de dados MySQL.
</p>
<ul>
  <li> Base: Python 3</li>
  <li> Dependências: Flask, requests, flask_mysqldb</li>
  <li> Banco de dados: MySQL rodando no host (configurado como <code>host.docker.internal</code>)</li>
  <li> Porta exposta: 5000</li>
  <li> Rotas:</li>
  <ul>
    <li><code>/</code>: Faz requisição GET para o container externo ou API externa</li>
    <li><code>/inserthost</code>: Insere no banco de dados um usuário obtido da API externa</li>
  </ul>
</ul>

<h3>🔗 3. Comunicação entre Containers</h3>
<p>
  O container host se comunica com o container externo ou API externa usando a biblioteca <code>requests</code>.  
  Para se conectar ao MySQL do host, usamos o endereço especial <code>host.docker.internal</code>, que aponta para o host da máquina Docker.
</p>

<h3>✅ 4. Fluxo de Dados</h3>
<ol>
  <li> O usuário acessa a rota <code>/</code> do container host.</li>
  <li> O container host faz uma requisição HTTP para o container externo ou API externa.</li>
  <li> Os dados retornados são processados e/ou armazenados no banco MySQL.</li>
  <li> O container host retorna o JSON final para o cliente.</li>
</ol>

<h3>⚙️ 5. Como Rodar</h3>
<p>
  <strong>Container Externo:</strong> <code>docker run -d -p 5001:5000 --name flaskexternacontainer flaskexterna</code><br>
  <strong>Container Host:</strong> <code>docker run -d -p 5000:5000 --name flaskhostcontainer flaskhost</code>
</p>

<hr/>

<h2>🤝 Conexão Entre Containers (Flask + MySQL)</h2>

<p>
  Além da comunicação com containers externos, também é possível conectar múltiplos containers em uma mesma <strong>network</strong>
  para que conversem entre si usando apenas o <em>nome do serviço</em>, sem precisar expor portas para o host.
</p>

<h3>🧱 1. Estrutura</h3>
<ul>
  <li><strong>MySQL Container:</strong> roda o banco de dados, inicializado com um <code>schema.sql</code> customizado.</li>
  <li><strong>Flask Container:</strong> expõe uma API com rotas que consomem dados externos e os inserem no MySQL.</li>
  <li><strong>Network:</strong> ambos os containers estão na mesma rede bridge (<code>flasknetwork</code>), o que permite comunicação por nome.</li>
</ul>

<h3>🐳 2. Dockerfiles</h3>

<strong>MySQL</strong> (<code>Dockerfile</code>):
<pre><code>FROM mysql:5.7

COPY schema.sql /docker-entrypoint-initdb.d/
EXPOSE 3306
VOLUME /backup/
</code></pre>

<strong>Flask</strong> (<code>Dockerfile</code>):
<pre><code>FROM python:3

WORKDIR /app
RUN pip install Flask requests flask_mysqldb
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
</code></pre>

<h3>⚙️ 3. Subindo os Containers</h3>

<p>Primeiro criamos a network:</p>
<pre><code>docker network create flasknetwork</code></pre>

<p>Depois subimos os serviços já conectados na mesma rede:</p>
<pre><code>docker run -d -p 3307:3306 --name mysql_api_container --network flasknetwork -e MYSQL_ROOT_PASSWORD=root mysqlnetworkapi
docker run -d -p 5000:5000 --name flask_api_container --rm --network flasknetwork flasknetworkapi
</code></pre>

<h3>🔗 4. Comunicação</h3>
<ul>
  <li>O container Flask acessa o MySQL pelo nome <code>mysql_api_container</code> na porta <code>3306</code>.</li>
  <li>Não é necessário mapear portas entre os containers, apenas para o host quando queremos acessar do Postman ou navegador.</li>
</ul>

<h3>🚀 5. Testando com Postman</h3>
<p>
  Ao enviar uma requisição <code>GET</code> para <code>http://localhost:5000/inserthost</code>, o container Flask consome dados externos
  (via <a href="https://randomuser.me/api" target="_blank">randomuser.me</a>) e insere registros no banco MySQL rodando no outro container.
</p>

<hr/>

<h2>🔗 6. Conectando e Desconectando Containers em Networks</h2>

<p>
  Caso você tenha criado uma network depois de subir um container, ou precise mover containers entre redes, 
  o Docker permite conectar ou desconectar containers a uma network existente.
</p>

<h3>🛠️ Conectar um container a uma network existente</h3>
<pre><code>docker network connect flasknetwork flask_api_container
docker network connect flasknetwork mysql_api_container
</code></pre>
<p>
  Com isso, ambos os containers estão na mesma network <code>flasknetwork</code> e podem se comunicar usando os nomes dos containers.
</p>

<h3>🛑 Desconectar um container de uma network</h3>
<pre><code>docker network disconnect flasknetwork flask_api_container
docker network disconnect flasknetwork mysql_api_container
</code></pre>
<p>
  Um container desconectado não consegue mais acessar outros containers nessa rede.
</p>

<hr/>

<h3>✅ 7. Fluxo Resumido da Comunicação</h3>
<ol>
  <li>Usuário faz requisição no endpoint Flask do container host (<code>/inserthost</code>).</li>
  <li>O container host Flask consome dados aleatórios do container externo ou da API externa.</li>
  <li>O host Flask conecta ao MySQL <em>pela network</em> e insere os dados recebidos.</li>
  <li>O MySQL persiste os registros no banco <code>flaskdocker</code>, disponíveis para consultas futuras.</li>
</ol>

<h2>📜 O que é YAML?</h2>
<p>
  <strong>YAML</strong> (YAML Ain’t Markup Language) é um formato de serialização de dados legível por humanos,
  muito usado em <strong>arquivos de configuração</strong>, como <code>docker-compose.yml</code>.
</p>
<ul>
  <li>✅ Legível e intuitivo (mais fácil que JSON/XML)</li>
  <li>✅ Suporte a listas, mapas (objetos), strings, números e booleanos</li>
  <li>✅ Permite comentários (ao contrário do JSON)</li>
  <li>✅ Usado em Docker, Kubernetes, CI/CD, Ansible e muito mais</li>
</ul>

<h2>🔑 Estrutura e Regras Básicas</h2>

<h3>📌 1. Indentação</h3>
<p>
  A identação é feita com <strong>espaços</strong> (nunca tabulação).  
  Cada nível representa hierarquia.
</p>
<pre><code>servico:
  nome: web
  porta: 8080
</code></pre>

<h3>💬 2. Comentários</h3>
<p>Usa-se <code>#</code> para comentar.</p>
<pre><code># Isto é um comentário
versao: "3.9"  # comentário inline
</code></pre>

<h3>📂 3. Tipos de Dados</h3>
<ul>
  <li><strong>Strings:</strong> <code>"texto"</code> ou <code>texto</code></li>
  <li><strong>Números:</strong> <code>idade: 30</code></li>
  <li><strong>Booleanos:</strong> <code>ativo: true</code></li>
  <li><strong>Nulos:</strong> <code>null</code> ou <code>~</code></li>
  <li><strong>Listas:</strong></li>
</ul>
<pre><code>frutas:
  - maçã
  - banana
  - uva
</code></pre>

<h2>🧩 Estruturas em YAML</h2>

<h3>🗂️ Mapas (Objetos)</h3>
<pre><code>usuario:
  nome: "Leo"
  email: "leo@example.com"
</code></pre>

<h3>📋 Listas de Objetos</h3>
<pre><code>servicos:
  - nome: mysql
    porta: 3306
  - nome: nginx
    porta: 80
</code></pre>

<h3>📝 Strings Multilinha</h3>
<pre><code>texto_preservado: |
  Linha 1
  Linha 2
  Linha 3

texto_unido: >
  Linha 1
  Linha 2
  Fica em uma única linha
</code></pre>

<h2>⚓ Recursos Avançados</h2>

<h3>🔗 Âncoras e Referências</h3>
<p>Permitem <strong>reutilizar configurações</strong> para evitar repetição.</p>
<pre><code>defaults: &padrao
  restart: always
  imagem: nginx:latest

web:
  <<: *padrao
  portas:
    - "8080:80"
</code></pre>

<h2>🐳 Exemplo no Docker Compose</h2>
<p>Um exemplo real de uso do YAML em um <code>docker-compose.yml</code>:</p>
<pre><code>version: "3.9"

services:
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: exemplo
      MYSQL_DATABASE: mydb
    ports:
      - "3306:3306"

  web:
    image: nginx:latest
    ports:
      - "8080:80"
    depends_on:
      - db
</code></pre>

<h3>⚠️ Erros Comuns</h2>
<ul>
  <li>🚫 Usar <strong>TAB</strong> em vez de espaço → erro de sintaxe</li>
  <li>🚫 Esquecer espaço depois de <code>-</code> em listas</li>
  <li>🚫 Strings ambíguas sem aspas (<code>yes/no, on/off</code>) podem virar booleanos</li>
</ul>

<h3>✅ Boas Práticas</h2>
<ul>
  <li>Use sempre 2 espaços por nível de indentação</li>
  <li>Adicione comentários explicativos</li>
  <li>Use âncoras para reduzir repetição</li>
  <li>Valide com <code>docker compose config</code> ou linters</li>
</ul>

<h2>📦 Docker Compose</h2>
<p>
  O <strong>Docker Compose</strong> é uma ferramenta que permite <em>definir e gerenciar múltiplos containers</em> como uma única aplicação.  
  Ele utiliza arquivos no formato <code>docker-compose.yml</code>, escritos em YAML, para descrever os serviços, redes e volumes necessários.  
  Isso facilita a criação de ambientes completos com apenas um comando.
</p>

<h3>🛠️ Como Funciona</h3>
<ul>
  <li>Você descreve os serviços (containers) no arquivo <code>docker-compose.yml</code>.</li>
  <li>O Compose cuida de criar os containers, volumes e redes automaticamente.</li>
  <li>Com um simples <code>docker compose up</code> você sobe toda a aplicação.</li>
</ul>

<h3>🐳 Exemplo WordPress + MySQL</h3>
<p>A seguir um exemplo de configuração para rodar o <strong>WordPress</strong> conectado a um banco de dados <strong>MySQL</strong>:</p>
<pre><code>version: "3.9"

services:
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: root123
      MYSQL_DATABASE: wordpress_db
      MYSQL_USER: wp_user
      MYSQL_PASSWORD: wp_pass
    volumes:
      - db_data:/var/lib/mysql
    restart: always

  wordpress:
    image: wordpress:latest
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wp_user
      WORDPRESS_DB_PASSWORD: wp_pass
      WORDPRESS_DB_NAME: wordpress_db
    depends_on:
      - db
    restart: always

volumes:
  db_data:
</code></pre>

<h3>🚀 Como Rodar</h3>
<ol>
  <li>Crie um arquivo chamado <code>docker-compose.yml</code> e cole o conteúdo acima.</li>
  <li>No terminal, execute:
    <pre><code>docker compose up -d</code></pre>
    Isso irá baixar as imagens necessárias e iniciar os containers em segundo plano.
  </li>
  <li>Acesse o navegador em <a href="http://localhost:8080">http://localhost:8080</a> e finalize a instalação do WordPress.</li>
</ol>

<h3>💻 Comandos Comuns do Docker Compose</h3>
<ul>
  <li>
    <pre><code>docker compose up</code></pre>
    Sobe os serviços definidos no <code>docker-compose.yml</code>.  
    Use a flag <code>-d</code> para rodar em segundo plano (modo <em>detached</em>).
  </li>

  <li>
    <pre><code>docker compose down</code></pre>
    Para e remove todos os containers, redes e volumes criados pelo Compose  
    (volumes nomeados não são removidos, a menos que use <code>--volumes</code>).
  </li>

  <li>
    <pre><code>docker compose stop</code></pre>
    Para os containers sem removê-los.  
    Eles podem ser reiniciados depois com <code>docker compose start</code>.
  </li>

  <li>
    <pre><code>docker compose ps</code></pre>
    Lista os serviços em execução e suas portas mapeadas.
  </li>

  <li>
    <pre><code>docker compose logs</code></pre>
    Exibe os logs de todos os serviços.  
    Use <code>-f</code> para acompanhar em tempo real.
  </li>

  <li>
    <pre><code>docker compose exec wordpress bash</code></pre>
    Executa um comando dentro de um container em execução.  
    Exemplo: abrir um terminal bash no serviço <code>wordpress</code>.
  </li>

  <li>
    <pre><code>docker compose build</code></pre>
    (Re)constrói as imagens definidas no Compose, útil após mudanças no <code>Dockerfile</code>.
  </li>
</ul>

<h3>⚙️ Variáveis de Ambiente no Docker Compose</h3>
<p>
O Docker Compose permite definir <strong>variáveis de ambiente</strong> para configurar os serviços sem expor senhas ou dados sensíveis diretamente no <code>docker-compose.yml</code>. 
Essas variáveis podem ser armazenadas em arquivos <code>.env</code> separados e referenciadas no serviço com a diretiva <code>env_file</code>.
</p>

<h4>📂 Exemplo de Arquivos</h4>
<p><strong>Arquivo <code>config/db.env</code></strong>:</p>
<pre><code>MYSQL_ROOT_PASSWORD=docker
MYSQL_DATABASE=wordpress
MYSQL_USER=docker
MYSQL_PASSWORD=docker
</code></pre>

<p><strong>Arquivo <code>config/wp.env</code></strong>:</p>
<pre><code>WORDPRESS_DB_HOST=db:3306
WORDPRESS_DB_USER=docker
WORDPRESS_DB_PASSWORD=docker
WORDPRESS_DB_NAME=wordpress
</code></pre>

<h4>📜 docker-compose.yml</h4>
<pre><code>services:
  db:
    image: mysql:8.0
    restart: always
    env_file:
      - ./config/db.env
    volumes:
      - db_data:/var/lib/mysql

  wordpress:
    image: wordpress:latest
    restart: always
    env_file:
      - ./config/wp.env
    ports:
      - "8080:80"
    depends_on:
      - db

volumes:
  db_data:
</code></pre>

<h4>✅ Benefícios</h4>
<ul>
  <li>Separa credenciais do código → mais seguro</li>
  <li>Facilita a troca de ambientes (desenvolvimento, teste, produção)</li>
  <li>Deixa o <code>docker-compose.yml</code> mais limpo</li>
</ul>

<h2>🌐 Redes no Docker Compose</h2>
<p>
O Docker Compose permite criar <strong>redes isoladas</strong> para que os containers se comuniquem de forma segura e organizada.
Cada serviço conectado a uma mesma rede pode acessar os outros usando o <code>nome do serviço</code> como hostname.
</p>

<h3>🔧 Exemplo com Rede Backend</h3>
<pre><code>services:
  db:
    image: mysql:8.0
    env_file:
      - ./config/db.env
    networks:
      - backend

  wordpress:
    image: wordpress:latest
    env_file:
      - ./config/wp.env
    networks:
      - backend
    ports:
      - "8080:80"

networks:
  backend:
    driver: bridge
</code></pre>

<h3>💡 Como Funciona</h3>
<ul>
  <li>Ambos os containers estão na mesma rede <code>backend</code></li>
  <li>O WordPress consegue acessar o MySQL usando o hostname <code>db</code> (nome do serviço)</li>
  <li>A rede <code>bridge</code> cria uma comunicação interna entre containers, isolada do host</li>
</ul>

<h3>✅ Benefícios</h3>
<ul>
  <li>Isolamento → containers só se comunicam com quem está na mesma rede</li>
  <li>Facilidade → acesso via hostname (ex: <code>db:3306</code>) sem precisar de IP fixo</li>
  <li>Flexibilidade → permite múltiplas redes em um mesmo projeto</li>
</ul>

<h3>⚠️ Erros Comuns</h3>
<ul>
  <li>🚫 Não mapear volumes → você perderá os dados do banco ao remover o container.</li>
  <li>🚫 Esquecer de configurar <code>depends_on</code> → o WordPress pode tentar conectar no MySQL antes dele iniciar.</li>
  <li>🚫 Senhas fracas → use variáveis de ambiente seguras em produção.</li>
</ul>

<h3>✅ Boas Práticas</h3>
<ul>
  <li>Use <strong>volumes nomeados</strong> (como <code>db_data</code>) para persistir dados.</li>
  <li>Sempre utilize <code>restart: always</code> para serviços críticos.</li>
  <li>Separe ambientes (ex.: <code>docker-compose.override.yml</code> para desenvolvimento).</li>
  <li>Valide seu arquivo com:
    <pre><code>docker compose config</code></pre>
  </li>
</ul>

<h2>🏗️ Build de Imagens no Docker Compose</h2>
<p>
O <strong>Docker Compose</strong> não serve apenas para orquestrar containers a partir de imagens já existentes, 
mas também pode <em>construir imagens personalizadas</em> automaticamente usando diretórios com <code>Dockerfile</code>.
</p>

<h3>🔧 Como Funciona</h3>
<ul>
  <li>Dentro do serviço, usamos a diretiva <code>build</code> em vez de <code>image</code>.</li>
  <li>O caminho definido em <code>build</code> deve conter um <code>Dockerfile</code> válido.</li>
  <li>Quando rodamos <code>docker compose up --build</code>, o Compose constrói a imagem antes de iniciar o container.</li>
</ul>

<h3>📂 Estrutura de Exemplo</h3>
<pre><code>compose_dockerfile_to_compose/
├── docker-compose.yml
├── mysql/
│   └── Dockerfile
└── flask/
    ├── app.py
    └── Dockerfile
</code></pre>

<h3>📜 docker-compose.yml</h3>
<pre><code>version: "3.9"

services:
  db:
    build: ./mysql/
    restart: always
    env_file:
      - ./config/db.env
    ports:
      - "3307:3306"
    networks:
      - dockercompose

  backend:
    build: ./flask/
    restart: always
    depends_on:
      - db
    ports:
      - "5000:5000"
    networks:
      - dockercompose

networks:
  dockercompose:
    driver: bridge
</code></pre>

<h3>🚀 Como Rodar</h3>
<ol>
  <li>No terminal, execute:
    <pre><code>docker compose up --build -d</code></pre>
    Isso irá construir as imagens <strong>mysqlcompose</strong> e <strong>flaskcompose</strong> a partir dos diretórios especificados.
  </li>
  <li>Para reconstruir após mudanças no Dockerfile:
    <pre><code>docker compose build</code></pre>
  </li>
  <li>Para forçar rebuild + iniciar containers:
    <pre><code>docker compose up --build</code></pre>
  </li>
</ol>

<h3>✅ Benefícios</h3>
<ul>
  <li>Permite criar imagens customizadas para cada serviço.</li>
  <li>Elimina a necessidade de rodar <code>docker build</code> manualmente.</li>
  <li>Facilita CI/CD, pois todo o processo de build e deploy fica no Compose.</li>
</ul>

<h2>📂 Bind Mount com Docker Compose</h2>
<p>
Um <strong>Bind Mount</strong> permite mapear um diretório do sistema operacional host para dentro de um container.
Assim, qualquer alteração feita nos arquivos locais é refletida imediatamente dentro do container.
Isso é muito útil em ambiente de <em>desenvolvimento</em>, pois evita rebuilds a cada mudança no código.
</p>

<h3>🔧 Como Configurar</h3>
<p>No <code>docker-compose.yml</code>, basta adicionar a diretiva <code>volumes</code> dentro do serviço desejado.</p>

<pre><code>services:
  backend:
    build: ./flask/
    restart: always
    volumes:
      - "C:\\Users\\leotr\\Documents\\Workspaces\\docker\\docker-learning\\compose_bind_mount\\flask:/app"
    depends_on:
      - db
    ports:
      - "5000:5000"
    networks:
      - dockercompose
</code></pre>

<h3>📜 Estrutura</h3>
<pre><code>compose_bind_mount/
├── docker-compose.yml
├── flask/          # Código Python local
│   └── app.py
└── mysql/
    └── Dockerfile
</code></pre>

<h3>⚡ Funcionamento</h3>
<ul>
  <li>A pasta local <code>flask/</code> é montada no diretório <code>/app</code> do container.</li>
  <li>Se você editar o arquivo <code>app.py</code> no host, a alteração aparece imediatamente dentro do container.</li>
  <li>Ideal para <strong>hot reload</strong> em frameworks como Flask.</li>
</ul>

<h3>✅ Benefícios</h3>
<ul>
  <li>Agilidade no desenvolvimento (sem rebuilds constantes).</li>
  <li>Facilidade para debugar e testar rapidamente.</li>
  <li>Integração direta entre código local e container.</li>
</ul>

<h3>⚠️ Observações</h3>
<ul>
  <li>No Windows, use o caminho completo com aspas duplas (<code>"C:\\Users\\..."</code>).</li>
  <li>No Linux/Mac, basta usar o caminho normal, ex: <code>./flask:/app</code>.</li>
  <li>Evite usar bind mounts em produção, prefira <strong>volumes gerenciados</strong> pelo Docker.</li>
</ul>

<h2>🌐 Docker Swarm</h2>
<p>
O <strong>Docker Swarm</strong> é a ferramenta nativa de <em>orquestração de containers</em> do Docker.
Ele permite transformar múltiplas máquinas (físicas ou virtuais) em um <strong>cluster</strong>, 
tratando-as como um único host lógico para execução de serviços.
</p>

<h3>🔧 Como Funciona</h3>
<ul>
  <li>Você inicializa um cluster com <code>docker swarm init</code>.</li>
  <li>Máquinas adicionais podem ser adicionadas como <strong>managers</strong> (responsáveis por orquestrar) ou <strong>workers</strong> (responsáveis por executar containers).</li>
  <li>Os serviços são distribuídos automaticamente entre os nós disponíveis.</li>
  <li>O Swarm garante <strong>alta disponibilidade</strong>, realocando containers caso algum nó falhe.</li>
</ul>

<h3>✅ Benefícios</h3>
<ul>
  <li>Escalabilidade horizontal: é possível aumentar ou reduzir a quantidade de réplicas facilmente.</li>
  <li>Balanceamento de carga automático entre containers de um mesmo serviço.</li>
  <li>Segurança: comunicação entre os nós do cluster é criptografada por padrão.</li>
  <li>Gestão simplificada, pois os comandos continuam sendo via <code>docker service</code> e <code>docker stack</code>.</li>
</ul>

<h3>⚠️ Observações</h3>
<ul>
  <li>O Docker Swarm é mais simples que o Kubernetes, mas também menos completo em termos de ecossistema e recursos avançados.</li>
  <li>Ideal para quem já usa Docker e precisa de <em>orquestração leve</em>.</li>
  <li>Indicado para ambientes menores ou médios, mas pode ser usado em produção.</li>
</ul>

<h2>🤖 Orquestração de Containers</h2>
<p>
A <strong>orquestração de containers</strong> é o processo de <em>gerenciar automaticamente</em> 
o ciclo de vida de múltiplos containers em ambientes distribuídos.
Isso inclui desde o <strong>deploy</strong> até o <strong>balanceamento, escalonamento e monitoramento</strong>.
</p>

<h3>🔧 O que Faz a Orquestração</h3>
<ul>
  <li><strong>Provisionamento</strong>: cria e inicializa containers em diferentes hosts.</li>
  <li><strong>Agendamento</strong>: decide em qual nó cada container deve rodar.</li>
  <li><strong>Escalonamento</strong>: aumenta ou reduz automaticamente a quantidade de réplicas de um serviço.</li>
  <li><strong>Monitoramento</strong>: acompanha o estado dos containers e reinicia se houver falhas.</li>
  <li><strong>Rede e comunicação</strong>: cria redes virtuais internas entre os serviços.</li>
  <li><strong>Balanceamento de carga</strong>: distribui requisições entre containers de forma eficiente.</li>
</ul>

<h3>✅ Principais Benefícios</h3>
<ul>
  <li>Alta disponibilidade e tolerância a falhas.</li>
  <li>Automatização do deploy e da recuperação de containers.</li>
  <li>Maior eficiência no uso de recursos de hardware.</li>
  <li>Possibilidade de rodar aplicações em ambientes de <em>produção escaláveis</em>.</li>
</ul>

<h3>📦 Ferramentas Populares</h3>
<ul>
  <li><strong>Docker Swarm</strong>: orquestrador nativo e simples de configurar.</li>
  <li><strong>Kubernetes</strong>: orquestrador mais robusto, com grande ecossistema e suporte de mercado.</li>
  <li><strong>Nomad</strong>: alternativa da HashiCorp, mais minimalista.</li>
</ul>

<h2>⚙️ Conceitos Fundamentais do Docker Swarm</h2>
<p>
Para entender como o <strong>Docker Swarm</strong> funciona, é essencial conhecer seus conceitos básicos.
Eles definem como os containers são organizados, distribuídos e executados dentro de um cluster.
</p>

<h3>🌐 Cluster</h3>
<p>
Um <strong>Cluster</strong> é o conjunto de máquinas (físicas ou virtuais) que trabalham em conjunto
para executar aplicações de forma distribuída e tolerante a falhas.  
No Docker Swarm, um cluster é composto por vários <em>nodes</em>, que podem ser managers ou workers.
</p>

<h3>🖥️ Nodes</h3>
<p>
Um <strong>Node</strong> é uma máquina que faz parte do cluster do Swarm.  
Cada node roda o Docker Engine e pode ser classificado como <em>manager</em> ou <em>worker</em>.
</p>
<ul>
  <li><strong>Manager Node</strong>: responsável por orquestrar e gerenciar o cluster.</li>
  <li><strong>Worker Node</strong>: responsável por executar as tarefas (containers) atribuídas pelos managers.</li>
</ul>

<h3>👑 Manager Nodes</h3>
<p>
Os <strong>manager nodes</strong> são os cérebros do cluster.  
Eles controlam a <em>orquestração</em> e a <em>tomada de decisões</em>, como:
</p>
<ul>
  <li>Agendamento de containers nos workers.</li>
  <li>Manutenção do estado desejado dos serviços.</li>
  <li>Replicação e tolerância a falhas.</li>
</ul>
<p>
Um cluster Swarm pode ter múltiplos managers para <strong>alta disponibilidade</strong>, mas apenas um atua como <em>Líder</em> (leader) usando o algoritmo de consenso <strong>Raft</strong>.
</p>

<h3>⚙️ Worker Nodes</h3>
<p>
Os <strong>worker nodes</strong> são os executores.  
Eles recebem instruções dos managers e rodam efetivamente os containers.  
Não tomam decisões por conta própria, apenas seguem as ordens enviadas.
</p>
<ul>
  <li>Executam <strong>tasks</strong> (instâncias de containers).</li>
  <li>Reportam status e métricas de volta para os managers.</li>
</ul>

<h3>🛠️ Services</h3>
<p>
Um <strong>Service</strong> é a definição de uma aplicação distribuída dentro do Swarm.  
Ele descreve o estado desejado, como:
</p>
<ul>
  <li>Qual imagem Docker deve ser usada.</li>
  <li>Quantas réplicas de containers devem rodar.</li>
  <li>Políticas de atualização e escalabilidade.</li>
</ul>
<p>
Na prática, um service é como um "plano" que o Swarm usa para criar e manter containers.
</p>

<h3>📦 Tasks</h3>
<p>
Uma <strong>Task</strong> é a menor unidade de execução no Swarm.  
Ela representa uma <em>instância de container</em> em execução, associada a um service.
</p>
<ul>
  <li>Cada task roda em um worker node.</li>
  <li>Se uma task falhar, o manager agenda automaticamente uma nova task em outro node.</li>
  <li>Um service em modo replicado pode ter várias tasks distribuídas no cluster.</li>
</ul>

<h3>✅ Resumindo</h3>
<ul>
  <li><strong>Cluster</strong>: conjunto de nodes que trabalham juntos no Swarm.</li>
  <li><strong>Node</strong>: máquina dentro do cluster.</li>
  <li><strong>Manager Node</strong>: orquestra e gerencia o cluster.</li>
  <li><strong>Worker Node</strong>: executa containers.</li>
  <li><strong>Service</strong>: definição da aplicação e estado desejado.</li>
  <li><strong>Task</strong>: container em execução, unidade prática do service.</li>
</ul>

<h2>🛤️ Maneiras de Executar o Docker Swarm</h2>
<p>
O Docker Swarm pode ser executado de diversas formas, dependendo do seu ambiente. 
Você pode rodá-lo localmente para testes, em nuvens como AWS, ou em labs dedicados como o Docker Labs. 
Isso permite flexibilidade: desde setups rápidos para desenvolvimento até clusters robustos em produção.
</p>
<h3>Opções Principais</h3>
<ul>
  <li><strong>Localmente (em múltiplas VMs ou máquinas físicas)</strong>: Use VMs no seu laptop com VirtualBox ou Hyper-V para simular um cluster.</li>
  <li><strong>Em Nuvem (ex: AWS, GCP, Azure)</strong>: Crie instâncias EC2 na AWS e configure o Swarm nelas para escalabilidade real.</li>
  <li><strong>Labs Online (ex: Docker Labs, Katacoda)</strong>: Ambientes pré-configurados para aprendizado sem setup manual.</li>
  <li><strong>Híbrido</strong>: Misture on-premise com nuvem para testes de failover.</li>
</ul>
<h3>Exemplo Prático</h3>
<p>
Para um setup local simples, crie três VMs (uma manager, duas workers) e siga os passos de inicialização. 
Isso é ideal para testar orquestração sem custos de nuvem.
</p>

<h2>☁️ Setup e Inicialização do Swarm na AWS e Docker Labs</h2>
<p>
Configurar o Docker Swarm na AWS ou em labs como o Docker Labs é uma ótima forma de praticar em ambientes realistas. 
Na AWS, usamos instâncias EC2 para simular nodes; no Docker Labs, tudo é pré-pronto. 
Vamos agrupar aqui o setup inicial, instalação do Docker e inicialização do cluster.
</p>
<h3>🔧 Setup na AWS</h3>
<ol>
  <li><strong>Criar Instâncias EC2</strong>: Lance 3 instâncias t2.micro (Ubuntu 20.04). Atribua IPs elásticos para acesso remoto.</li>
  <li><strong>Configurar Security Groups</strong>: Abra portas TCP 22 (SSH), 2377 (Swarm init), 7946 (comunicação nodes) e 4789/UDP (overlay network).</li>
  <li><strong>Instalar Docker</strong>: Em cada instância, rode <code>sudo apt update &amp;&amp; sudo apt install docker.io -y</code>, inicie o serviço com <code>sudo systemctl start docker</code> e adicione seu usuário ao grupo docker: <code>sudo usermod -aG docker $USER</code>.</li>
</ol>
<p>
Exemplo de comando para instalar Docker em uma instância AWS: 
<code>curl -fsSL https://get.docker.com -o get-docker.sh &amp;&amp; sh get-docker.sh</code>.
</p>
<h3>🔧 Setup no Docker Labs</h3>
<ol>
  <li>Acesse <a href="https://labs.play-with-docker.com/">Docker Labs</a> e crie uma sessão com múltiplos nodes (ex: 3 nodes).</li>
  <li>Docker já está pré-instalado; basta clonar seu repo ou preparar imagens.</li>
  <li>Use o terminal integrado para comandos Swarm.</li>
</ol>
<p>
Exemplo: No Lab, selecione "Swarm" mode e os nodes aparecem prontos para <code>docker swarm init</code>.
</p>
<h3>🚀 Inicializando o Swarm</h3>
<p>
No manager node (ex: primeira instância AWS ou node1 no Lab), rode:
</p>
<pre><code>docker swarm init --advertise-addr &lt;IP_DO_MANAGER&gt;</code></pre>
<p>
Isso gera tokens para workers. Exemplo de saída:
<code>docker swarm join --token SWMTKN-1-abc123xyz789 192.0.2.1:2377</code>.
</p>
<p>
Verifique com <code>docker info</code> – deve mostrar "Swarm: active".
</p>

<h2>📊 Gerenciando Nodes: Listando, Adicionando e Removendo</h2>
<p>
Gerenciar nodes é crucial para manter o cluster saudável. Vamos cobrir listagem, adição e remoção, 
incluindo recuperação de tokens e drenagem de nodes.
</p>
<h3>📋 Listando Todos os Nodes</h3>
<p>
Use <code>docker node ls</code> no manager para ver todos os nodes, seu status (Ready/Shutdown), role (Manager/Worker) e disponibilidade.
</p>
<pre><code>$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
abc123 *                      manager1            Ready               Active              Leader              20.10.12
def456                        worker1             Ready               Active                                  20.10.12
ghi789                        worker2             Ready               Active                                  20.10.12</code></pre>
<h3>➕ Adicionando Máquinas ao Swarm</h3>
<ol>
  <li>No manager, pegue o token worker: <code>docker swarm join-token worker</code>.</li>
  <li>No novo worker, rode o comando join gerado.</li>
</ol>
<p>
Exemplo para adicionar um worker AWS: SSH na instância e execute o join token.
</p>
<h3>🔑 Recuperando o Token do Manager</h3>
<p>
Para adicionar outro manager: <code>docker swarm join-token manager</code>. 
Isso gera um token seguro para promoção de workers a managers, garantindo consenso Raft.
</p>
<h3>🚫 Deixando o Swarm em um Node</h3>
<p>
Em um worker: <code>docker swarm leave</code>. Para forçar em manager: <code>docker swarm leave --force</code>.
</p>
<h3>🗑️ Removendo um Node</h3>
<ol>
  <li>Drenar tasks: <code>docker node update --availability drain &lt;NODE_ID&gt;</code> (para não receber novas tasks).</li>
  <li>Remover: <code>docker node rm &lt;NODE_ID&gt;</code>.</li>
</ol>
<p>
Exemplo: <code>docker node update --availability drain def456</code> seguido de <code>docker node rm def456</code>.
</p>
<h3>⏹️ Parando de Receber Tasks em um Node</h3>
<p>
Use <code>docker node update --availability drain &lt;NODE_ID&gt;</code> para pausar agendamento de novas tasks, 
permitindo drenar gradualmente. Reative com <code>--availability active</code>.
</p>

<h2>🛠️ Deploy e Gerenciamento de Serviços</h2>
<p>
Deployar serviços é o coração do Swarm. Vamos ver como subir, verificar, remover, replicar, inspecionar e escalar.
</p>
<h3>🚀 Subindo um Serviço no Swarm</h3>
<p>
Crie um serviço com <code>docker service create</code>. Exemplo: Deployar um Nginx com 3 réplicas:
</p>
<pre><code>docker service create --name web-nginx --replicas 3 -p 80:80 nginx:latest</code></pre>
<p>
Isso roda 3 containers Nginx, balanceados na porta 80 do cluster.
</p>
<h3>🔍 Verificando Serviços Rodando no Swarm</h3>
<p>
<code>docker service ls</code> lista serviços, réplicas e status.
</p>
<pre><code>$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
abc123              web-nginx           replicated          3/3                 nginx:latest        *:80->80/tcp</code></pre>
<h3>🗑️ Removendo Serviços</h3>
<p>
<code>docker service rm &lt;SERVICE_NAME&gt;</code>. Exemplo: <code>docker service rm web-nginx</code>. 
Isso para todas as tasks e remove o serviço.
</p>
<h3>🔄 Replicando Serviços</h3>
<p>
Especifique <code>--replicas N</code> no create ou atualize com <code>docker service scale web-nginx=5</code>.
</p>
<pre><code>docker service update --replicas 5 web-nginx</code></pre>
<p>
O Swarm distribui as novas réplicas nos nodes disponíveis.
</p>
<h3>📊 Testando a Orquestração do Swarm</h3>
<p>
Acesse via IP do manager (porta 80). Para testar failover: Pare um worker com <code>docker node update --availability drain worker1</code> 
e veja o Swarm realocar tasks automaticamente. Monitore com <code>docker service ps web-nginx</code>.
</p>
<h3>🔎 Inspecionando Serviços</h3>
<p>
<code>docker service inspect &lt;SERVICE&gt;</code> mostra detalhes como tasks, rede e updates. 
Exemplo: <code>docker service inspect web-nginx --pretty</code> exibe em formato legível.
</p>
<h3>🐳 Verificando Quais Containers Estão Rodando</h3>
<p>
  <code>docker ps</code> em um node mostra tasks locais. 
  Para global: <code>docker service ps &lt;SERVICE&gt;</code>.
</p>
<pre><code>$ docker service ps web-nginx
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE
</code></pre>

<h2>📈 Escalando e Atualizando Aplicações</h2>
<p>
  Escalar e atualizar são chave para produção. Inclui Compose no Swarm e updates de imagem.
</p>

<h3>📝 Compose no Swarm</h3>
<p>
  Docker Compose funciona no Swarm com <code>docker stack deploy</code>. 
  Crie um <code>docker-compose.yml</code>:
</p>
<pre><code>version: '3.8'
services:
  web:
    image: nginx
    deploy:
      replicas: 3
    ports:
      - "80:80"
</code></pre>
<p>
  Deploy: <code>docker stack deploy -c docker-compose.yml myapp</code>. 
  Liste stacks com <code>docker stack ls</code>.
</p>

<h3>📊 Escalando Nossa Aplicação</h3>
<p>
  Atualize réplicas no Compose: <code>docker service scale myapp_web=5</code>. 
  O Swarm ajusta automaticamente, balanceando carga.
</p>

<h3>🔄 Atualizando uma Imagem no Swarm</h3>
<ol>
  <li>Atualize o service: <code>docker service update --image nginx:1.21 web-nginx</code>.</li>
  <li>O Swarm rola updates gradualmente (rolling update) para zero downtime.</li>
</ol>
<p>
  Exemplo com política: 
  <code>docker service update --update-parallelism 1 --update-delay 10s web-nginx</code> 
  atualiza 1 task a cada 10s.
</p>

<h2>🌐 Redes e Conectividade no Swarm</h2>
<p>
  Redes overlay permitem comunicação segura entre serviços em nodes diferentes.
</p>

<h3>🔗 Criando Redes para Serviços do Swarm</h3>
<p>
  Crie uma rede overlay: 
  <code>docker network create --driver overlay minha-rede</code>.
</p>
<p>
  No service: 
  <code>docker service create --name app --network minha-rede alpine ping google.com</code>.
</p>

<h3>🔌 Conectando Serviço a uma Rede Já Existente</h3>
<p>
  Atualize: <code>docker service update --network-add minha-rede web-nginx</code>.
</p>
<p>
  Exemplo: Conecte dois serviços (web e db) na mesma rede para comunicação interna via nomes de serviço 
  (ex: web acessa db via "db:5432").
</p>

<h3>📚 Conclusão Swarm</h2>
<p>
  Para aprofundar, consulte a 
  <a href="https://docs.docker.com/engine/swarm/" target="_blank">
    documentação oficial do Docker Swarm
  </a>. 
  Ela cobre tópicos avançados como secrets, configs e integração com CI/CD.
</p>
<p>
  O Docker Swarm transforma Docker em uma solução de orquestração poderosa e acessível. 
  Com conceitos como services, tasks e nodes, você pode deployar apps escaláveis com alta disponibilidade. 
</p>
<hr/>

<h2>☸️ 1. O que é Kubernetes?</h2>
<p>
  O <strong>Kubernetes</strong> (ou <em>K8s</em>) é uma plataforma open-source criada pela Google 
  para <strong>orquestração de containers</strong>. 
  Ele automatiza processos como <em>deploy</em>, <em>escalonamento</em>, <em>disponibilidade</em> 
  e <em>gerenciamento</em> de aplicações em containers, tornando mais fácil rodar aplicações distribuídas e de alta escala.
</p>
<p>
  Em vez de gerenciar manualmente cada container (como fazemos no Docker puro), o Kubernetes cuida da 
  <strong>infraestrutura de execução</strong>, garantindo que sua aplicação esteja sempre rodando como esperado,
  mesmo em caso de falhas em servidores ou containers individuais.
</p>

<hr/>

<h2>📚 2. Principais Conceitos do Kubernetes</h2>

<h3>🧠 Control Plane</h3>
<p>
  É o "cérebro" do Kubernetes, responsável por decidir onde e como os containers vão rodar.  
  Ele controla o estado desejado do cluster, garantindo que os recursos sejam aplicados corretamente.
</p>

<h3>🖥️ Nodes</h3>
<p>
  São as máquinas (físicas ou virtuais) que compõem o cluster.  
  Cada node roda um agente chamado <code>kubelet</code>, responsável por gerenciar os pods nesse node.
</p>

<h3>📦 Pods</h3>
<p>
  São as <strong>menores unidades do Kubernetes</strong>.  
  Um Pod pode conter um ou mais containers que compartilham recursos (rede, armazenamento, etc).  
  Normalmente, cada pod executa uma parte específica da aplicação.
</p>

<h3>🚀 Deployments</h3>
<p>
  Um <code>Deployment</code> define <strong>como e quantos pods</strong> da sua aplicação devem ser executados.  
  Ele também cuida de <em>updates</em> e <em>rollbacks</em>, garantindo atualizações sem downtime.
</p>

<h3>🌐 Services</h3>
<p>
  São a forma de expor os Pods para comunicação interna ou externa.  
  Como os Pods são efêmeros (podem morrer e renascer), o Service atua como um <strong>ponto estável</strong> de acesso.
</p>

<h3>💻 kubectl</h3>
<p>
  É a <strong>CLI (Command Line Interface)</strong> usada para interagir com o cluster Kubernetes.  
  Comandos como <code>kubectl get pods</code> ou <code>kubectl apply -f deployment.yaml</code> 
  permitem gerenciar todos os recursos do cluster.
</p>

<h3>🗂️ Namespaces</h3>
<p>
  São divisões lógicas dentro do cluster.  
  Eles permitem organizar e isolar recursos entre diferentes equipes, ambientes (dev, test, prod) ou aplicações.
</p>

<h3>📦 ConfigMaps e Secrets</h3>
<p>
  Recursos usados para <strong>gerenciar configurações e credenciais</strong> das aplicações no cluster.  
  <code>ConfigMaps</code> armazenam dados de configuração, enquanto <code>Secrets</code> guardam informações sensíveis (ex: senhas, tokens).
</p>

<h3>📊 ReplicaSets</h3>
<p>
  Garante que um número específico de réplicas de Pods esteja sempre em execução.  
  É usado por trás dos Deployments para manter a alta disponibilidade.
</p>

<h3>✅ Resumindo</h3>
<ul>
  <li><strong>Control Plane</strong>: componente central que gerencia o cluster.</li>
  <li><strong>Node</strong>: máquina (física ou VM) que executa pods.</li>
  <li><strong>Pod</strong>: menor unidade do Kubernetes, encapsula um ou mais containers.</li>
  <li><strong>Deployment</strong>: controla a criação, atualização e replicação de pods.</li>
  <li><strong>Service</strong>: expõe pods de forma estável via rede (ClusterIP, NodePort, LoadBalancer).</li>
  <li><strong>Namespace</strong>: organiza e isola recursos dentro do cluster.</li>
  <li><strong>kubectl</strong>: ferramenta de linha de comando para interagir com o cluster.</li>
</ul>

<h2>⚙️ Dependências Necessárias para Rodar Kubernetes</h2>

<p>
  Para começar a trabalhar com Kubernetes em ambiente local ou de testes, você precisa instalar algumas ferramentas essenciais:
</p>

<h3>🔑 Principais Dependências</h3>
<ul>
  <li><strong>kubectl</strong>: CLI oficial para interagir com clusters Kubernetes (criar, gerenciar e inspecionar recursos).</li>
  <li><strong>Minikube</strong>: ferramenta que cria um cluster Kubernetes local em sua máquina (ideal para estudos e testes).</li>
  <li><strong>Virtualização</strong>: necessária para rodar Minikube (pode usar Hyper-V, VirtualBox, Docker Driver ou KVM, dependendo do sistema).</li>
</ul>

<h3>💻 Instalação no Windows</h3>
<ol>
  <li>Instale um driver de virtualização:
    <ul>
      <li><strong>Hyper-V</strong> (Windows Pro/Enterprise)</li>
      <li><strong>Docker Desktop</strong> (pode ser usado como driver)</li>
    </ul>
  </li>
  <li>Instale o <code>kubectl</code>:
    <pre><code>choco install kubernetes-cli</code></pre>
    (usando <a href="https://chocolatey.org/" target="_blank">Chocolatey</a>)
  </li>
  <li>Instale o <code>minikube</code>:
    <pre><code>choco install minikube</code></pre>
  </li>
  <li>Verifique:
    <pre><code>kubectl version --client
minikube version</code></pre>
  </li>
</ol>

<h3>🐧 Instalação no Linux</h3>
<ol>
  <li>Instale o <code>kubectl</code>:
    <pre><code>curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/</code></pre>
  </li>
  <li>Instale o <code>minikube</code>:
    <pre><code>curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube</code></pre>
  </li>
  <li>Verifique:
    <pre><code>kubectl version --client
minikube version</code></pre>
  </li>
</ol>

<h3>🚀 Iniciando o Cluster</h3>
<p>
  Após instalar, basta iniciar o cluster local com:
</p>
<pre><code>minikube start</code></pre>
<p>
  Isso cria um cluster Kubernetes de nó único em sua máquina, pronto para rodar seus <em>pods</em>, <em>services</em> e <em>deployments</em>.
</p>

<h3>🛠️ Comandos Essenciais do Minikube</h3>
<ul>
  <li><strong>Iniciar o cluster com driver Docker:</strong>
    <pre><code>minikube start --driver=docker</code></pre>
  </li>
  <li><strong>Parar o cluster:</strong>
    <pre><code>minikube stop</code></pre>
  </li>
  <li><strong>Deletar o cluster:</strong>
    <pre><code>minikube delete</code></pre>
  </li>
  <li><strong>Acessar o painel gráfico (dashboard):</strong>
    <pre><code>minikube dashboard</code></pre>
  </li>
  <li><strong>Ver status do cluster:</strong>
    <pre><code>minikube status</code></pre>
  </li>
  <li><strong>Listar IP do cluster:</strong>
    <pre><code>minikube ip</code></pre>
  </li>
</ul>

<h3>🛠️ Comandos Essenciais do kubectl</h3>
<ul>
  <li><strong>Listar todos os nodes do cluster:</strong>
    <pre><code>kubectl get nodes</code></pre>
  </li>
  <li><strong>Listar todos os pods:</strong>
    <pre><code>kubectl get pods</code></pre>
  </li>
  <li><strong>Listar pods com mais detalhes:</strong>
    <pre><code>kubectl get pods -o wide</code></pre>
  </li>
  <li><strong>Descrever um pod específico:</strong>
    <pre><code>kubectl describe pod &lt;nome-do-pod&gt;</code></pre>
  </li>
  <li><strong>Ver logs de um pod:</strong>
    <pre><code>kubectl logs &lt;nome-do-pod&gt;</code></pre>
  </li>
  <li><strong>Acessar o terminal de um pod:</strong>
    <pre><code>kubectl exec -it &lt;nome-do-pod&gt; -- /bin/bash</code></pre>
  </li>
  <li><strong>Criar um deployment:</strong>
    <pre><code>kubectl create deployment meu-app --image=nginx</code></pre>
  </li>
  <li><strong>Escalar réplicas de um deployment:</strong>
    <pre><code>kubectl scale deployment meu-app --replicas=3</code></pre>
  </li>
  <li><strong>Deletar um deployment:</strong>
    <pre><code>kubectl delete deployment meu-app</code></pre>
  </li>
    <li><strong>Exibir configuração completa:</strong>
    <pre><code>kubectl config view</code></pre>
  </li>
  <li><strong>Ver contexto atual:</strong>
    <pre><code>kubectl config current-context</code></pre>
  </li>
  <li><strong>Listar todos os contextos configurados:</strong>
    <pre><code>kubectl config get-contexts</code></pre>
  </li>
</ul>

<h2>⚙️ 3. Deployments e Services no Kubernetes</h2>

<h3>🚀 Deployments</h3>
<p>
  Um <strong>Deployment</strong> define como a aplicação deve ser executada no cluster, incluindo:
</p>
<ul>
  <li>Qual imagem de container usar</li>
  <li>Quantas réplicas de pods devem existir</li>
  <li>Como atualizar a aplicação sem downtime</li>
</ul>
<p>
  Ele garante que o estado desejado seja mantido: se algum pod falhar, o Deployment cria outro automaticamente.
</p>
<p><strong>Exemplo prático:</strong></p>
<pre><code>kubectl create deployment flask-deployment --image=leonardotrevisol/flask-kub-project</code></pre>
<p>
  Esse comando cria um Deployment chamado <code>flask-deployment</code> que executa um pod com a imagem especificada.
</p>

<h3>🌐 Services</h3>
<p>
  Os <strong>Services</strong> permitem expor os pods para comunicação interna ou externa.  
  Como os pods são efêmeros, o Service fornece um ponto de acesso estável, podendo ser:
</p>
<ul>
  <li><strong>ClusterIP</strong>: acesso interno dentro do cluster</li>
  <li><strong>NodePort</strong>: expõe a aplicação em uma porta do node</li>
  <li><strong>LoadBalancer</strong>: cria um IP externo para acesso público (quando disponível)</li>
</ul>
<p><strong>Exemplo prático:</strong></p>
<pre><code>kubectl expose deployment flask-deployment --type=LoadBalancer --port=5000</code></pre>
<p>
  Esse comando cria um Service do tipo <code>LoadBalancer</code> que expõe a aplicação na porta 5000, permitindo que seja acessada externamente.
</p>

<h3>💡 Fluxo Prático</h3>
<ol>
  <li>Criar o Deployment com a imagem do container: <code>kubectl create deployment</code></li>
  <li>Verificar os pods criados: <code>kubectl get pods</code></li>
  <li>Criar um Service para expor os pods: <code>kubectl expose deployment</code></li>
  <li>Verificar o Service e IP externo (se LoadBalancer): <code>kubectl get services</code></li>
  <li>Acessar a aplicação via navegador ou curl usando o IP/porta fornecidos</li>
</ol>

<h2>🛠️ Comandos Essenciais para Deployments e Services</h2>

<h3>📦 Deployments</h3>
<ul>
  <li><strong>Criar um Deployment:</strong>
    <pre><code>kubectl create deployment meu-app --image=nginx</code></pre>
  </li>
  <li><strong>Listar Deployments:</strong>
    <pre><code>kubectl get deployments</code></pre>
  </li>
  <li><strong>Escalar um Deployment (alterar réplicas):</strong>
    <pre><code>kubectl scale deployment meu-app --replicas=3</code></pre>
  </li>
  <li><strong>Atualizar a imagem de um Deployment:</strong>
    <pre><code>kubectl set image deployment/meu-app meu-app=nginx:latest</code></pre>
  </li>
  <li><strong>Deletar um Deployment:</strong>
    <pre><code>kubectl delete deployment meu-app</code></pre>
  </li>
  <li><strong>Ver detalhes de um Deployment:</strong>
    <pre><code>kubectl describe deployment meu-app</code></pre>
  </li>
</ul>

<h3>🌐 Services</h3>
<ul>
  <li><strong>Expor Deployment como Service ClusterIP (interna):</strong>
    <pre><code>kubectl expose deployment meu-app --type=ClusterIP --port=80</code></pre>
  </li>
  <li><strong>Expor Deployment como Service NodePort (externa em porta alta):</strong>
    <pre><code>kubectl expose deployment meu-app --type=NodePort --port=80</code></pre>
  </li>
  <li><strong>Expor Deployment como Service LoadBalancer (externa em IP externo):</strong>
    <pre><code>kubectl expose deployment meu-app --type=LoadBalancer --port=80</code></pre>
  </li>
  <li><strong>Listar Services:</strong>
    <pre><code>kubectl get services</code></pre>
  </li>
  <li><strong>Ver detalhes de um Service:</strong>
    <pre><code>kubectl describe service meu-app</code></pre>
  </li>
  <li><strong>Deletar um Service:</strong>
    <pre><code>kubectl delete service meu-app</code></pre>
  </li>
</ul>

<h2>🚀 Escalando a Aplicação</h3>
  <ul>
    <li><strong>Aumentar ou reduzir réplicas:</strong> Ajuste o número de pods de um <em>Deployment</em> para suportar picos de tráfego ou economizar recursos.
      <pre><code>kubectl scale deployment flask-deployment --replicas=5</code></pre>
    </li>
    <li><strong>Verificar réplicas:</strong> Liste os pods em execução para confirmar o escalonamento.
      <pre><code>kubectl get pods -o wide</code></pre>
      <p class="note"><strong>Dica:</strong> Use <code>-o wide</code> para ver detalhes como o nó onde o pod está rodando.</p>
    </li>
    <li><strong>Reduzir réplicas:</strong> Diminua o número de pods ativos.
      <pre><code>kubectl scale deployment flask-deployment --replicas=2</code></pre>
    </li>
  </ul>

  <h3>🔄 Atualizando e Revertendo Deployments</h3>
  <ul>
    <li><strong>Atualizar imagem do container:</strong> Atualize para uma nova versão da imagem sem recriar o <em>Deployment</em>.
      <pre><code>kubectl set image deployment/flask-deployment flask-container=leonardotrevisol/flask-kub-project:v2</code></pre>
    </li>
    <li><strong>Reverter atualização:</strong> Volte à versão anterior em caso de problemas.
      <pre><code>kubectl rollout undo deployment/flask-deployment</code></pre>
      <p class="note"><strong>Nota:</strong> Veja o histórico de revisões com <code>kubectl rollout history deployment/flask-deployment</code>.</p>
    </li>
  </ul>

  <h3>📜 Modo Declarativo: Gerenciando com YAML</h3>
  <ul>
    <li><strong>Aplicar configuração YAML:</strong> Defina o estado desejado do cluster em um arquivo YAML e aplique com <code>kubectl apply</code>.
      <pre><code>kubectl apply -f deployment.yaml</code></pre>
      <p class="note"><strong>Vantagem:</strong> Ideal para versionamento em repositórios Git e automação em pipelines CI/CD.</p>
    </li>
  </ul>
  <div class="example-box">
    <strong>Exemplo de YAML para um Deployment:</strong>
    <pre><code>apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-deployment
  labels:
    app: flask
spec:
  replicas: 3
  selector:
    matchLabels:
      app: flask
  template:
    metadata:
      labels:
        app: flask
    spec:
      containers:
      - name: flask-container
        image: leonardotrevisol/flask-kub-project:v1
        ports:
        - containerPort: 5000
</code></pre>
  </div>

  <h3>♻️ Atualizando o Projeto</h3>
<p>Para atualizar sua aplicação no Kubernetes, você precisa criar uma nova versão da imagem Docker, enviar para o Docker Hub, atualizar a tag no arquivo YAML do Deployment e aplicar a alteração no cluster.</p>

<ul>
  <li><strong>1. Construir nova imagem com nova tag:</strong><br/>
    <code>docker build -t leonardotrevisol/flask-kub-project:v2 .</code>
  </li>

  <li><strong>2. Enviar imagem para o Docker Hub:</strong><br/>
    <code>docker push leonardotrevisol/flask-kub-project:v2</code>
  </li>

  <li><strong>3. Atualizar a tag da imagem no Deployment YAML:</strong><br/>
    No arquivo <code>deployment.yaml</code>, altere a linha do container para usar a nova tag:<br/>
    <code>image: leonardotrevisol/flask-kub-project:v2</code>
  </li>

  <li><strong>4. Aplicar a atualização no cluster:</strong><br/>
    <code>kubectl apply -f deployment.yaml</code>
  </li>

  <li><strong>5. Verificar se os pods foram atualizados:</strong><br/>
    <code>kubectl get pods</code><br/>
    <code>kubectl rollout status deployment flask-deployment</code>
  </li>

  <li><strong>6. Reverter caso algo dê errado:</strong><br/>
    <code>kubectl rollout undo deployment flask-deployment</code>
  </li>
</ul>

  <h3>🔑 Principais Campos em Arquivos YAML</h3>
  <ul>
    <li><strong>apiVersion:</strong> Versão da API do Kubernetes (ex.: <code>apps/v1</code>).</li>
    <li><strong>kind:</strong> Tipo de recurso (ex.: <code>Deployment</code>, <code>Service</code>, <code>Pod</code>).</li>
    <li><strong>metadata:</strong> Informações como nome, namespace e labels.</li>
    <li><strong>spec:</strong> Configuração desejada (réplicas, imagem, portas, etc.).</li>
    <li><strong>status:</strong> Estado atual do recurso (gerado pelo Kubernetes).</li>
  </ul>

  <h3>💡 Dicas Práticas</h3>
  <ul>
    <li>Use <code>kubectl describe deployment flask-deployment</code> para detalhes do estado de um <em>Deployment</em>.</li>
    <li>Monitore eventos do cluster com <code>kubectl get events</code> para diagnosticar problemas.</li>
    <li>Para automação, combine o modo declarativo com ferramentas como Helm ou Kustomize.</li>
  </ul>


