# 🤖 Auto_Python: automação de cadastro de produtos (RPA)

Script em **Python** que simula uma pessoa usando o computador: abre o navegador, faz login num sistema web e **cadastra automaticamente todos os produtos de uma planilha CSV**, sem intervenção manual.

Projeto feito durante o Intensivão de Python da Hashtag Treinamentos, como prática de automação de tarefas repetitivas (RPA).

## 🎯 Problema que resolve

Cadastrar centenas de produtos à mão num sistema sem API é lento e sujeito a erro. O script lê a base de dados e preenche o formulário linha por linha, do mesmo jeito que uma pessoa faria, só que mais rápido e sem errar a digitação.

## ⚙️ Como funciona

1. Abre o Google Chrome e acessa o sistema de login
2. Preenche e-mail e senha e entra no sistema
3. Lê o arquivo `produtos.csv` com **Pandas**
4. Para cada produto, preenche os campos: código, marca, tipo, categoria, preço unitário, custo e observação (quando existir)
5. Envia o formulário, volta ao topo da página e repete até acabar a lista

## 🛠️ Tecnologias

- **Python 3**
- **PyAutoGUI**: controle de mouse e teclado
- **Pandas**: leitura e manipulação do CSV

## ▶️ Como executar

```bash
git clone https://github.com/Flaviobll/Auto_Python.git
cd Auto_Python
pip install -r requirements.txt
python codigo.py
```

> ⚠️ Durante a execução, não mexa no mouse nem no teclado. Para abortar, leve o mouse rapidamente para o canto superior esquerdo da tela (failsafe do PyAutoGUI).

## 📁 Arquivos

| Arquivo | Função |
|---|---|
| `codigo.py` | Script principal da automação |
| `auxiliar.py` | Mostra a posição atual do mouse, para descobrir as coordenadas (x, y) dos cliques |
| `produtos.csv` | Base de produtos a cadastrar |
| `requirements.txt` | Dependências do projeto |

## 📝 Observações

- As coordenadas de clique (x, y) dependem da resolução da tela. Use o `auxiliar.py` para ajustá-las na sua máquina.
- O navegador precisa ficar em foco durante a execução.
- O `produtos.csv` deve estar na mesma pasta do script.

---
Feito por [Flávio Barbosa](https://www.linkedin.com/in/flaviobarbosaa).
