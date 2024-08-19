import random
import requests

# Function to Generate weather Report
def get_weather():
    city_name = input("Enter the name of the city you want the weather report for: ")

    # Generate report directly within get_weather
    url = 'https://wttr.in/{}'.format(city_name)
    try:
        data = requests.get(url)
        T = data.text
    except Exception as e:
        T = f"Error occurred: {e}"
    print(T)

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the math book look sad? It had too many problems.",
        "What do you call fake spaghetti? An impasta!"
    ]
    return random.choice(jokes)
