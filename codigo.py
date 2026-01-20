# bibliotecas = pacotes de código
# pip install pyautogui

import pyautogui
import time

#pyautogui.click -> clica
#pyautogui.write -> escreve um texto
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -> aperta um atalho (hotkey)
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3) # pyautogui hashtag

# Passo 2: Fazer login
# clicar no campo de email
pyautogui.click(x=468, y=412)
pyautogui.write("qualqueremail@gmail.com")
pyautogui.press("tab") # passar para o proximo campo
pyautogui.write("qualquersenha")
pyautogui.press("tab")
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: # Para cada linha da minha tabela
    # Passo 4: Cadastrar 1 produto
    # codigo
    pyautogui.click(x=516, y=294) # clicar no campo do código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # passar para o proximo campo
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # passar para o botão enviar

    pyautogui.press("enter") # clicou no botão enviar
    # voltar para o início da tela
    pyautogui.scroll(5000)


# Passo 5: Repetir o passo 4 até acabar a lista de produtos