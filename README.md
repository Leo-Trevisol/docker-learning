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
    <li>essenciais de terminal/Linux</li>
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
      <strong>-it</strong>: Executa o container em modo interativo com terminal.<br>
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
      <pre><code>docker start [nome_ou_id]</code></pre>
      Reinicia um container que está parado.
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
      Remove uma imagem do seu sistema.
    </li>
  </ul>

  <h3>✅ Resumindo</h3>
  <ul>
    <li>Procure imagens no <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>.</li>
    <li>Use <code>docker run</code> para executar containers.</li>
    <li>Use <code>-it</code> para interagir com o container.</li>
    <li>Use <code>-d</code> para rodar containers em background.</li>
    <li>Use <code>--name [nome]</code> para dar nomes aos containers.</li>
    <li>Use <code>--rm</code> para remover automaticamente containers temporários.</li>
    <li>Use <code>docker start [nome_ou_id]</code> para reiniciar containers parados.</li>
    <li>Use <code>docker stop [nome_ou_id]</code> para parar containers em execução.</li>
    <li>Use <code>docker rm [nome_ou_id]</code> para remover containers parados.</li>
    <li>Use <code>docker rm -f [nome_ou_id]</code> para forçar a remoção de containers em execução.</li>
    <li>Use <code>docker logs [nome_ou_id]</code> para ver os logs de um container.</li>
    <li>Use <code>docker logs -f [nome_ou_id]</code> para acompanhar logs em tempo real.</li>
    <li>Com <code>docker ps</code> e <code>docker images</code> você monitora o que está rodando no seu sistema.</li>
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

<h3>🌐 Expondo portas no container</h3>
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

  <h3>📦 Criando a Imagem</h3>
  <p>
    Para criar a imagem a partir do <code>Dockerfile</code>, use o comando:
  </p>
  <pre><code>docker build -t meu-app-node .</code></pre>
  <ul>
    <li><strong>-t meu-app-node</strong>: dá o nome <em>meu-app-node</em> para a imagem.</li>
    <li><strong>.</strong>: indica que o <code>Dockerfile</code> está no diretório atual.</li>
  </ul>

  <h3>🐳 Rodando o Container</h3>
  <p>
    Depois que a imagem for criada, você pode rodar um container com:
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

  <h3>✅ Resumindo</h3>
  <ul>
    <li>Escreva um <code>Dockerfile</code> com as instruções da sua aplicação.</li>
    <li>Use <code>docker build -t nome-imagem .</code> para criar a imagem.</li>
    <li>Use <code>docker run -p porta:porta nome-imagem</code> para rodar um container.</li>
    <li>Seu app estará acessível no navegador pela porta que você expôs.</li>
  </ul>
</section>


