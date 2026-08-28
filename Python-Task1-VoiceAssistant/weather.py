import requests

from config import WEATHER_API_KEY
from services.logger import logger


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Fetch current weather information for a city.
    Returns a user-friendly message instead of crashing.
    """

    if not WEATHER_API_KEY:
        logger.error("Weather API key is missing.")

        return (
            "The weather service is not configured. "
            "Please check the weather API key."
        )

    if not city or not city.strip():
        logger.warning("Weather request received without a city.")

        return "Please provide a city name."

    city = city.strip()

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        location = data["name"]

        logger.info(
            f"Weather retrieved successfully for city: {location}"
        )

        return (
            f"The weather in {location} is {description}. "
            f"The temperature is {temperature:.1f} degrees Celsius, "
            f"feels like {feels_like:.1f} degrees, "
            f"with {humidity} percent humidity."
        )

    except requests.exceptions.HTTPError as error:

        status_code = error.response.status_code

        logger.error(
            f"Weather API HTTP error for '{city}': "
            f"{status_code}"
        )

        if status_code == 401:
            return (
                "The weather API key is invalid "
                "or has not been activated yet."
            )

        if status_code == 404:
            return f"I couldn't find a city named {city}."

        if status_code == 429:
            return (
                "The weather service request limit "
                "has been reached. Please try again later."
            )

        return (
            "The weather service returned an error. "
            "Please try again later."
        )

    except requests.exceptions.Timeout:

        logger.error(
            f"Weather API timeout for city: {city}"
        )

        return (
            "The weather service took too long to respond. "
            "Please try again."
        )

    except requests.exceptions.ConnectionError as error:

        logger.error(
            f"Weather connection error: {error}"
        )

        return (
            "I couldn't connect to the weather service. "
            "Please check your internet connection."
        )

    except requests.exceptions.RequestException as error:

        logger.error(
            f"Weather request error: {error}"
        )

        return (
            "There was a problem connecting to "
            "the weather service."
        )

    except (KeyError, TypeError, ValueError) as error:

        logger.error(
            f"Unexpected weather API response: {error}"
        )

        return (
            "I received an unexpected response "
            "from the weather service."
        )

    except Exception as error:

        logger.exception(
            f"Unexpected weather error: {error}"
        )

        return (
            "Something went wrong while getting "
            "the weather."
        )