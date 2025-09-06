<?php

// Pega o valor enviado pelo formulário via método POST
$message = $_POST['message'];

// Lê os arquivos dentro da pasta "messages"
// A função scandir() retorna um array com todos os arquivos e pastas
$files = scandir('./messages');

// Conta quantos arquivos existem na pasta
// "- 2" porque o scandir sempre retorna "." (diretório atual) e ".." (diretório pai)
$num_files = count($files) - 2;

// Define o nome do próximo arquivo de mensagem
// Exemplo: msg-0.txt, msg-1.txt, msg-2.txt ...
$file_name = "msg-{$num_files}.txt";

// Cria um novo arquivo em modo exclusivo ('x')
// Se já existir um arquivo com o mesmo nome, vai gerar erro
$file = fopen("./messages/{$file_name}", 'x');

// Escreve a mensagem dentro do arquivo
fwrite($file, $message);

// Fecha o arquivo (boa prática para liberar recursos)
fclose($file);

// Redireciona de volta para a página index.php após salvar a mensagem
header('Location: index.php');
