from datetime import datetime
import core
import random
import requests
import pyjokes

# Receber informações do clima.
def get_weather():
    city_name = input("\nEnter the name of the city or press ENTER to use current location: ")

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

# Manual
def help():
    # Printa um textao explicando o app ou abre um arquivo .txt?
    return "Here is what you can do with me:"