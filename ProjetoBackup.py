# janela para selecionar a pasta do nosso computador
import os
from tkinter.filedialog import askdirectory
import shutil
import datetime

# Solicita ao usuário que selecione a pasta para fazer o backup
nome_pasta_selecionada = askdirectory()

# Obtém a lista de arquivos e pastas na pasta selecionada
lista_arquivos = os.listdir(nome_pasta_selecionada)

# Define o nome e o caminho da pasta de backup
nome_pasta_backup = "backup"
nome_completo_pasta_backup = f"{nome_pasta_selecionada}/{nome_pasta_backup}"

# Cria a pasta de backup se ela não existir
if not os.path.exists(nome_completo_pasta_backup): 
    os.mkdir(nome_completo_pasta_backup)

# Obtém a data e hora atuais para criar uma subpasta com data e hora
data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")

# Itera sobre cada arquivo e pasta na pasta selecionada
for arquivo in lista_arquivos:
    nome_completo_arquivo = f"{nome_pasta_selecionada}/{arquivo}"
    nome_final_arquivo = f"{nome_completo_pasta_backup}/{data_atual}/{arquivo}"

    # Cria a subpasta com a data e hora atuais
    if not os.path.exists(f"{nome_completo_pasta_backup}/{data_atual}"):
        os.mkdir(f"{nome_completo_pasta_backup}/{data_atual}")
        
    # Verifica se o item é um arquivo ou uma pasta e faz o backup apropriado
    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo) #Serve para copiar arquivos
    elif "backup" != arquivo:
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo) #Serve para copiar pastas

