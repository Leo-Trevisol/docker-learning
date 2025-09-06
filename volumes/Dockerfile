# Define a imagem base a ser usada: PHP 8 com Apache já configurado
FROM php:8-apache

# Define o diretório de trabalho dentro do container
# Todos os próximos comandos (COPY, RUN, etc.) serão executados a partir daqui
WORKDIR /var/www/html/

# Copia todos os arquivos do diretório atual (host) para dentro do container
# O "." da esquerda é a pasta local e o "." da direita é o WORKDIR no container
# Isso coloca o código do projeto na pasta /var/www/html/
COPY . .

# Expõe a porta do container para acesso externo
# ⚠️ Aqui está escrito "8", mas deveria ser "80", que é a porta padrão do Apache
EXPOSE 80

# Ajusta as permissões dos arquivos para o usuário www-data (usuário padrão do Apache no Debian/Ubuntu)
# O "-R" aplica de forma recursiva (em todos os arquivos e pastas)
# ⚠️ Tem um erro de digitação: "chwon" → o correto é "chown"
RUN chown -R www-data:www-data /var/www
