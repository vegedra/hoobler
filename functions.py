import random
import requests

# Receber informações do clima.
def get_weather():
    city_name = input("\nEnter the name of the city you want the weather report for: ")

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

# Conta piadas
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the math book look sad? It had too many problems.",
        "What do you call fake spaghetti? An impasta!"
    ]
    return random.choice(jokes)
