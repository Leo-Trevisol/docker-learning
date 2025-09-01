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
    <li>Comandos essenciais de terminal/Linux</li>
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
    Ele precisa estar aberto para que os comandos <code>docker</code> funcionem no terminal
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
  <p>Para abrir um terminal dentro do container e testar comandos Linux:</p>
  <pre><code>docker run --rm -it ubuntu bash</code></pre>
  <ul>
    <li><strong>-it</strong>: abre o container em modo interativo com terminal.</li>
    <li>Dentro do shell do container, você pode rodar comandos Linux normalmente.</li>
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
  <h2>📦 Imagens Docker e Comandos Básicos</h2>

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

  <h3>⚙️ Comandos básicos</h3>
  <p>Aqui estão alguns comandos essenciais para começar:</p>
  <ul>
    <li>
      <pre><code>docker run --rm -it ubuntu bash</code></pre>
      <strong>-it</strong>: Executa o container em modo interativo com terminal.
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
      <pre><code>docker images</code></pre>
      Lista todas as imagens disponíveis localmente.
    </li>
    <li>
      <pre><code>docker rmi [imagem]</code></pre>
      Remove uma imagem do seu sistema.
    </li>
  </ul>

  <h3>✅ Resumindo</h3>
  <ul>
    <li>Procure imagens no <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>.</li>
    <li>Use <code>docker run</code> para executar containers.</li>
    <li>Use <code>-it</code> para interagir com o container.</li>
    <li>Digite <code>exit</code> para sair de um container interativo.</li>
    <li>Com <code>docker ps</code> e <code>docker images</code> você monitora o que está rodando no seu sistema.</li>
  </ul>
</section>




