import importlib.resources
import src.core
import os
import json

# Função para criar o arquivo de configuração padrão
def criar_configuracao():
    print("Hoobler: Arquivo de configurações não encontrado.")
    print("Hoobler: Iniciando setup.")
    with open("configs.txt", "w") as f:
        f.write("""# Configurações do HOOBLER
# Defina o idioma: 'pt' para Português, 'en' para Inglês, etc.
idioma=None

# Defina a interface: 'cli' para Linha de Comando, 'gui' para Interface Gráfica
interface=None
""")
    print("Hoobler: Arquivo de configurações criado. Por favor, defina as preferências:\n")
    config()  # Chama a função para atualizar as configurações

# Função para configurar e atualizar o arquivo de configuração
def config():
    configuracoes = {}
    with open('configs.txt', 'r') as f:
        linhas = f.readlines()
        
    alterado = False

    # Solicitar idioma
    idioma_atual = next((linha for linha in linhas if linha.startswith('idioma=')), None)
    if idioma_atual and 'None' in idioma_atual:
        print("Digite 'pt' para definir o idioma em português:")
        print("Type 'en' to set the program in English:")
        idioma = input("> ").strip()
        configuracoes['idioma'] = idioma
        alterado = True
    else:
        configuracoes['idioma'] = idioma_atual.split('=')[1].strip() if idioma_atual else 'None'

    # Solicitar interface
    interface_atual = next((linha for linha in linhas if linha.startswith('interface=')), None)
    if interface_atual and 'None' in interface_atual:
        print("Digite 'cli' para Linha de Comando ou 'gui' para Interface Gráfica:")
        interface = input("> ").strip()
        configuracoes['interface'] = interface
        alterado = True
    else:
        configuracoes['interface'] = interface_atual.split('=')[1].strip() if interface_atual else 'None'
    
    # Atualizar o arquivo com as novas configurações
    if alterado:
        with open('configs.txt', 'w') as f:
            for linha in linhas:
                if linha.startswith('idioma='):
                    f.write(f"idioma={configuracoes['idioma']}\n")
                elif linha.startswith('interface='):
                    f.write(f"interface={configuracoes['interface']}\n")
                else:
                    f.write(linha)
        print("Hoobler: Configurações atualizadas!")

# Função para carregar configurações
def carregar_configuracoes():
    configuracoes = {}
    try:
        with open('configs.txt', 'r') as f:
            linhas = f.readlines()

        for linha in linhas:
            if linha.startswith('idioma='):
                configuracoes['idioma'] = linha.split('=')[1].strip()
            elif linha.startswith('interface='):
                configuracoes['interface'] = linha.split('=')[1].strip()

    except FileNotFoundError:
        print("Hoobler: Arquivo de configurações não encontrado. Usando configurações padrão.")
        configuracoes['idioma'] = 'pt'  # Valor padrão
        configuracoes['interface'] = 'cli'  # Valor padrão

    return configuracoes

# Função para aplicar configurações
def aplicar_configuracoes(configuracoes):
    global idioma
    global interface

    idioma = configuracoes.get('idioma', 'pt')
    interface = configuracoes.get('interface', 'cli')

    if idioma == 'pt':
        print("Idioma definido para Português.")
        # Implemente a lógica para definir o idioma para Português
    elif idioma == 'en':
        print("Language set to English.")
        # Implemente a lógica para definir o idioma para Inglês
    else:
        print("Error.")

    if interface == 'cli':
        print("Interface definida para Linha de Comando.")
        # Implemente a lógica para usar a interface CLI
    elif interface == 'gui':
        print("Interface set to Graphical User Interface.")
        # Implemente a lógica para usar a interface GUI
    else:
        print("Error.")