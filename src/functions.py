from datetime import datetime
from src.calc import Calculator
from nltk.corpus import wordnet
import nltk
import src.core
import os
import sys
import random
import requests
import pyjokes

# Get the parent directory of the current file (src folder)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to the sys.path
sys.path.append(parent_dir)

# Now you can import main
import main

# Receber informações do clima.
def get_weather():
    city_name = input("\nHoobler: Enter the name of the city or press ENTER to use current location: ")

    # Usa o sistema WTTR para ver o clima - ?T - Remove cor e faz arte ASCII funcionar e o 0 para mostrar apenas
    # o clima atual
    url = 'https://wttr.in/{}?T&0'.format(city_name)
    try:
        data = requests.get(url)
        T = data.text
    except Exception as e:
        T = f"Error occurred: {e}"
    # Printa o clima e a arte ASCII
    return T

# Conta piadas - TODO: OPÇÃO DE IDIOMAS E PIADAS SEM SER DE T.I.
def tell_joke(): 
    # Usa a biblioteca Pyjokes para gerar piadas de T.I.
    jokes = pyjokes.get_jokes(language="en", category="all") 
    
    # Retorna uma piada aleatoria da lista de piadas criadas acima
    return random.choice(jokes)
    
# Fala a hora
def tell_time():
    # Recebe a data e hora atual
    now = datetime.now()

    # Formata a data de um jeito mais elegante
    date = now.strftime("%A - %B %d, %Y")  # e.g., "Wednesday, August 21, 2024"

    return f"It's {date}."

# Calculadora simples
def calc():
    calcular = Calculator()
    line = input("Hoobler: Type math account\n> ")
    
    try:
        print("Hoobler:", calcular.parse(line))
    except SyntaxError as e:
        print(f'Hoobler: {e.msg}')

    ch = input("Hoobler: Do you want to use the calculator again? y/n\n> ")
    if ch.lower() in ('s', 'y'):
        conta = 0
        return calc()
    else: 
        return "Ok."
        
def roll_dice():
    faces = input("Hoobler: How many faces?\n> ")
    try:
        faces = int(faces.strip())
        if faces < 1:
            raise ValueError("Number of faces must be at least 1.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None
    
    dice = random.randint(1, faces)
    return "The dice rolled a... ", dice

def tell_definition():
    word = input("> ")
    synsets = wordnet.synsets(word)

    if synsets:
        print(f"Hoobler: Definitions for '{word}':")
        for synset in synsets:
            return f" - {synset.definition()}"
    else:
        return f"No definitions found for '{word}'."
        
# Manual
def help():
    return """I'm a chatbot that can learn with you. Here are some things I can do:
    1. I can tell you the weather (type 'weather');
    2. I can tell you a tech joke (type 'joke');
    3. I can tell you the time (type 'time');
    4. I can tell the definition of a word and what it is (type 'what is');
    5. I can be a calculator (type 'calc');
    6. I can roll you a dice for a random number (type 'dice');
    7. To clear the screen type 'cls'.
    
These are some of the things I can do for you, beside chatting."""

# Limpar tela
def cls():
    os.system('cls')
    return "Cleared!"