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


