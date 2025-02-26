# Gerenciador de Backup

Este repositório contém um script em Python que realiza o backup de arquivos e pastas de um diretório escolhido pelo usuário. O script cria uma subpasta chamada **backup** e, dentro dela, uma pasta com data e hora do momento em que o backup foi feito.

## Descrição

- O script abre uma janela para o usuário selecionar uma pasta do computador.
- Em seguida, lista todos os arquivos e subpastas do diretório selecionado.
- Cria (caso não exista) uma pasta chamada **backup** dentro do diretório escolhido.
- Dentro dessa pasta de backup, cria uma subpasta com o formato de data e hora atual, por exemplo: `2025-02-26 103045`.
- Copia todos os arquivos e subpastas para a subpasta de backup recém-criada, preservando metadados (data de modificação, etc.).
- Ignora a própria pasta **backup** para evitar copiar backups anteriores recursivamente.

## Pré-requisitos

- [Python 3.x](https://www.python.org/downloads/) instalado na máquina.
- A biblioteca **tkinter** vem por padrão em muitas distribuições do Python (especialmente no Windows). Se estiver em Linux ou macOS e não tiver o tkinter instalado, pode ser necessário instalá-lo separadamente:
  - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
  - **Fedora**: `sudo dnf install python3-tkinter`
  - **macOS**: Geralmente já vem incluído com a instalação padrão do Python (se não, instale o Python oficial do site python.org).

## Como executar

1. **Clone ou baixe** este repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/Gerenciador-de-Backup.git

