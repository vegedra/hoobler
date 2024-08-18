import json
from difflib import get_close_matches

# TODO: Abrir programas, responder perguntas (wikipedia), ser mais esperto
# e uma certa aleatoriedade na escolha das respostas ve com o chatgpt

# Carrega o arquivo JSON com a base da IA
def load_knowledge_base(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
    
# Salva o que a IA aprende no arquivo JSON
def save_knowledge_base(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        
# Encontra a melhor resposta para o que o usuario escreve
def find_best_match(user_question, questions):
    matches= get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None
    
# Responde com a melhor resposta encontrada
def get_answer(question, knowledge_base):
    for q in knowledge_base["questions"]:
        return q["answer"]
        
# Main Program
def chat_bot():
    # Carrega o JSON
    knowledge_base = load_knowledge_base('knowledge_base.json')
    
    # Main Loop
    while True:
        # Recebe input do usuario
        user_input = input('> ')
        
        # Para fechar o programa
        if user_input.lower() == 'quit':
            break
        
        # Procura a melhor resposta
        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        
        # Responde
        if best_match:
            answer = get_answer(best_match, knowledge_base)
            print(f'Hoobler: {answer}')
        # Não encontrou melhor resposta
        else: 
            # Pergunta se o usuario quer ensinar como responder
            print("Hoobler: I don\'t know the answer. Teach me.")
            new_answer = input("Type the answer or 'skip': ")
            
            # Se quiser armazena resposta do jogador no arquivo JSON
            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Hoobler: Thank you.')
                
if __name__ == '__main__':
    chat_bot()