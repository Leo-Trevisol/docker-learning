<section id="o-que-voce-vai-aprender">
  <h2>📚 O que irei aprender neste curso</h2>

  <h3>Fundamentos do Docker</h3>
  <ul>
    <li>O que é Docker e para que serve</li>
    <li>Instalação e configuração</li>
    <li>Principais comandos do Docker</li>
  </ul>

  <h3>Containers e Imagens</h3>
  <ul>
    <li>Criação e execução de containers</li>
    <li>Criação, atualização e gerenciamento de imagens</li>
    <li>Copiando arquivos (como imagens) de/para containers usando o comando <code>cp</code></li>
    <li>Publicação de imagens no Docker Hub</li>
  </ul>

  <h3>Gerenciamento de Recursos</h3>
  <ul>
    <li>Volumes e persistência de dados</li>
    <li>Bind Mount</li>
    <li>Criação e utilização de networks</li>
    <li>Conexão externa: host ↔ containers e entre containers</li>
  </ul>

  <h3>Docker Compose</h3>
  <ul>
    <li>Gerenciamento de múltiplos containers</li>
    <li>Criação de ambientes completos com Compose</li>
  </ul>

  <h3>Projetos Práticos</h3>
  <ul>
    <li>Aplicações em <strong>PHP</strong>, <strong>Python</strong>, <strong>JavaScript</strong> e outras tecnologias</li>
    <li>Estruturação de projetos dockerizados</li>
  </ul>

  <h3>YAML para Docker e Kubernetes</h3>
  <ul>
    <li>Estrutura e sintaxe</li>
    <li>Modo declarativo e imperativo</li>
  </ul>

  <h3>Orquestração com Docker Swarm</h3>
  <ul>
    <li>Instalação e configuração</li>
    <li>Criação e atualização de projetos no Swarm</li>
    <li>Replicação de serviços</li>
    <li>Uso de Docker Compose no Swarm</li>
  </ul>

  <h3>Orquestração com Kubernetes</h3>
  <ul>
    <li>Instalação e uso do Minikube</li>
    <li>Conceitos fundamentais de Kubernetes</li>
    <li>Criação e gerenciamento de projetos</li>
    <li>Escalabilidade e orquestração de containers</li>
  </ul>

  <h3>Linux e Terminal</h3>
  <ul>
    <li>Essenciais de terminal/Linux</li>
    <li>Aplicação prática no uso do Docker</li>
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

<h3>✅ 6. Fluxo Resumido</h3>
<ol>
  <li>Usuário faz requisição no endpoint Flask (<code>/inserthost</code>).</li>
  <li>Flask busca dados aleatórios na API externa.</li>
  <li>Flask conecta no MySQL <em>dentro da network</em> e salva os dados.</li>
  <li>MySQL persiste os registros no banco <code>flaskdocker</code>.</li>
</ol>



