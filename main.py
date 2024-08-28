from difflib import get_close_matches
import config as cfg
import importlib.resources
import src.core
import os
import json
import sys
import random

""" TODO: 
Abrir programas;
Responder perguntas (wikipedia); 
Lidar com erro de localizacao invalida do wttr;
Tentar escolher as respostas baseadas em contexto. """

# Variáveis globais para armazenar configurações
idioma = 'en'  # Valor padrão
interface = 'cli'  # Valor padrão

# Função principal do chat bot
def main():
    # Verifica se o arquivo JSON existe
    try:
        with importlib.resources.open_text('src', 'knowledge_base.json') as file:
            knowledge_base = json.load(file)
    except FileNotFoundError:
        print("Error loading knowledge base: knowledge_base.json not found.")
        return
    print("\n------- HOOBLER --------\n   by Pedro Ivo, 2024")
    
    # Loop principal
    while True:
        user_input = input('\n> ').strip()

        # Para fechar o programa
        if user_input.lower() in ('quit', 'sair', 'bye', 'tchau', 'adeus', 'goodbye', 'exit'):
            print("Hoobler: See you later!")
            break
        elif user_input.lower() in ('remove question', 'remove entry'):
            question_to_remove = input('Which question would you like to remove? ')
            src.core.remove_question_from_knowledge_base(question_to_remove, knowledge_base)
            continue

        # Procura a melhor resposta
        best_match = src.core.find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        # Responde
        if best_match:
            answer = src.core.get_answer(user_input, knowledge_base)
            print(f'Hoobler: {answer}')
        else:
            print("Hoobler: I don't know the answer. Can you teach me?")
            new_answer = input("Type the answer or 'skip': ")

            if new_answer.lower() != 'skip':
                src.core.add_or_update_question(knowledge_base, user_input, new_answer)
                src.core.save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Hoobler: Thank you.')

if __name__ == '__main__':
    if not os.path.exists('configs.txt'):
        cfg.criar_configuracao()
    else:
        configuracoes = cfg.carregar_configuracoes()
        cfg.aplicar_configuracoes(configuracoes)
    main()