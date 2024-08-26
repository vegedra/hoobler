from difflib import get_close_matches
import os
import sys
import json
import random

# Obtém o caminho absoluto da pasta raiz (Hoobler)
base_dir = os.path.dirname(__file__)

# Construindo o caminho para a pasta "src"
src_dir = os.path.join(base_dir, 'src')

# Adiciona o diretório "src" ao sys.path
sys.path.append(src_dir)

from core import *
import config as cfg
import functions  

""" TODO: 
Abrir programas;
Responder perguntas (wikipedia); 
Ser mais esperto;
Modo terapia/ELIZA;
Tentar implementar um SPELL CHECKER;
Lidar com erro de localizacao invalida do wttr;
Tentar escolher as respostas baseadas em contexto. """

# Main Program
def chat_bot():
    knowledge_base = load_knowledge_base('knowledge_base.json')
    
    if cfg.values['setup'] == 0:
        setup()
    else:
        # Main Loop
        while True:
            # Recebe input do usuario e remove espaços
            user_input = input('> ').strip()

            # Para fechar o programa
            if user_input.lower() in ('quit', 'sair', 'bye', 'tchau', 'adeus', 'goodbye', 'exit'):
                print("Hoobler: See you later!")
                break
            elif user_input.lower() in ('remove question', 'remove entry'):
                question_to_remove = input('Which question would you like to remove? ')
                remove_question_from_knowledge_base(question_to_remove, knowledge_base)
                continue
            

            # Procura a melhor resposta
            best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

            # Responde
            if best_match:
                answer = get_answer(user_input, knowledge_base)
                print(f'Hoobler: {answer}')
            # Não encontrou melhor resposta
            else:
                # Pergunta se o usuario quer ensinar como responder
                print("Hoobler: I don't know the answer. Can you teach me?")
                new_answer = input("Type the answer or 'skip': ")

                # Se o usuario aceitar, armazena resposta do jogador no arquivo JSON
                if new_answer.lower() != 'skip':
                    add_or_update_question(knowledge_base, user_input, new_answer)
                    save_knowledge_base('knowledge_base.json', knowledge_base)
                    print('Hoobler: Thank you.')

def setup():
    print("1) Português")
    print("2) English")
    
    # input
    while True:
        key = input()

        if key.lower() == '1':
            cfg.values['current_language'] = 'pt_BR'
            break
        elif key.lower() == '2':
            cfg.values['current_language'] = 'en'
            break
    
    print("Escolha o modo de exibição:")
    print("1) CLI")
    print("2) GUI")
    
    # input
    while True:
        key = input()

        if key.lower() == '0':
            cfg.values['mode'] = 0
            break
        elif key.lower() == '1':
            cfg.values['mode'] = 1
            break
    cfg.values['setup'] = 1
    print(cfg.values)
    chat_bot()

if __name__ == '__main__':
    chat_bot()