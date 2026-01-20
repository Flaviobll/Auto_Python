📄 Descrição do Arquivo codigo.py

Este arquivo é um script de automação desenvolvido em Python que simula a interação humana com o navegador para realizar o cadastro automático de produtos em um sistema web.

A automação utiliza a biblioteca PyAutoGUI para controlar teclado e mouse, e a biblioteca Pandas para leitura e manipulação de dados a partir de um arquivo CSV.

⚙️ O que o script faz, passo a passo

Abre o navegador automaticamente

Simula o pressionamento da tecla Windows

Abre o Google Chrome

Acessa a URL do sistema de login da empresa

Realiza o login no sistema

Preenche automaticamente o campo de e-mail

Preenche a senha

Envia o formulário de login

Aguarda o carregamento da página

Importa uma base de dados (produtos.csv)

Lê um arquivo CSV contendo os dados dos produtos

Armazena as informações em uma tabela usando Pandas

Cadastra produtos automaticamente no sistema
Para cada linha da planilha, o script:

Preenche os campos:

Código

Marca

Tipo

Categoria

Preço unitário

Custo

Observações (quando existente)

Envia o formulário

Retorna ao início da página para o próximo cadastro

Repete o processo até finalizar todos os registros

O loop percorre toda a base de dados

Cada produto é cadastrado sem intervenção manual

🧠 Objetivo do Script

O objetivo principal deste arquivo é automatizar tarefas repetitivas de cadastro, reduzindo erros humanos, economizando tempo e aumentando a produtividade em processos administrativos.

Esse tipo de solução é ideal para:

Sistemas que não possuem API

Cadastros manuais em grande volume

Automação de processos (RPA)

🛠️ Tecnologias Utilizadas

Python

PyAutoGUI – automação de mouse e teclado

Pandas – leitura e manipulação de dados

CSV – base de dados de entrada

⚠️ Observações Importantes

As coordenadas de clique (x e y) podem variar de acordo com a resolução da tela.

É necessário manter o navegador em foco durante a execução do script.

O arquivo produtos.csv deve estar no mesmo diretório do script.
