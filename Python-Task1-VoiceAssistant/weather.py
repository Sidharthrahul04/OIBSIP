import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    if not API_KEY:
        return "Weather API key is not configured."

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            return f"I couldn't find a city named {city}."

        response.raise_for_status()

        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        return (
            f"The weather in {city} is {description}. "
            f"The temperature is {temperature:.1f} degrees Celsius, "
            f"feels like {feels_like:.1f} degrees, "
            f"with {humidity} percent humidity."
        )

    except requests.exceptions.Timeout:
        return "The weather service took too long to respond."

    except requests.exceptions.ConnectionError:
        return "I couldn't connect to the weather service."

    except requests.exceptions.RequestException as error:
        return f"Weather API error: {error}"