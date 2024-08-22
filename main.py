from difflib import get_close_matches
from core import *
import json
import random
import functions  

""" TODO: 
Abrir programas;
Responder perguntas (wikipedia); 
Ser mais esperto;
Modo terapia/ELIZA;
Tentar implementar um SPELL CHECKER;
Tentar escolher as respostas baseadas em contexto. """

# Main Program
def chat_bot():
    knowledge_base = load_knowledge_base('knowledge_base.json')

    # Main Loop
    while True:
        # Recebe input do usuario e remove espaços
        user_input = input('> ').strip()

        # Para fechar o programa
        if user_input.lower() in ('quit', 'sair'):
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

if __name__ == '__main__':
    chat_bot()