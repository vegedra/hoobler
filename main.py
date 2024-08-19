from difflib import get_close_matches
import json
import random
import functions  

""" TODO: 
Abrir programas;
Responder perguntas (wikipedia); 
Ser mais esperto;
Modo terapia/ELIZA. """

# Carrega o arquivo JSON com a base da IA
def load_knowledge_base(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Verifica a estrutura do JSON
            if not isinstance(data, dict) or "questions" not in data:
                raise ValueError("Invalid JSON structure")
            return data
    except (json.JSONDecodeError, FileNotFoundError, ValueError) as e:
        print(f"Error loading knowledge base: {e}")
        return {"questions": []}

# Salva o que a IA aprende no arquivo JSON
def save_knowledge_base(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
    except IOError as e:
        print(f"Error saving knowledge base: {e}")

# Encontra a melhor resposta para o que o usuario escreve
def find_best_match(user_question, questions):
    # Encontra strings que são "parecidas" com uma string alvo, a partir de uma lista 
    # de possibilidades e transforma a lista de perguntas em uma única lista de strings para comparação""" 
    flattened_questions = [q for sublist in questions for q in sublist]
    matches = get_close_matches(user_question.lower(), [q.lower() for q in flattened_questions], n=1, cutoff=0.6)
    return matches[0] if matches else None

# Responde com a melhor resposta encontrada
def get_answer(user_question, knowledge_base):
    for q in knowledge_base["questions"]:
        # Verifica se user_questions coincide com alguma pergunta na lista
        if any(question.lower() in user_question.lower() for question in q["question"]):
            if "function" in q:
                func_name = q["function"]
                func = getattr(functions, func_name, None)
                if func:
                    return func()
            return random.choice(q["answer"])
    return "I don't understand that question."

# Adiciona uma nova resposta a uma pergunta existente ou cria uma nova entrada
def add_or_update_question(knowledge_base, user_question, new_answer):
    for q in knowledge_base["questions"]:
        if any(question.lower() == user_question.lower() for question in q["question"]):
        # Verifica se a resposta já existe na lista
            if new_answer not in q["answer"]:
                q["answer"].append(new_answer)
            return
    # Se a pergunta não existir, adiciona uma nova entrada
    knowledge_base["questions"].append({"question": [user_question], "answer": [new_answer]})

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