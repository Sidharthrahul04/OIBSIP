import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

from intents import detect_intent
from weather import get_weather
from reminders import set_reminder


recognizer = sr.Recognizer()


def speak(text):
    print("Assistant:", text)

    # Create a fresh TTS engine for every response
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
        return ""

    except sr.RequestError:
        print("Sorry, there was a problem with the speech recognition service.")
        return ""


while True:

    command = listen()

    if not command:
        continue

    result = detect_intent(command)

    intent = result["intent"]
    entities = result["entities"]

    # Greeting
    if intent == "GREETING":
        speak("Hello! How can I help you?")

    # Time
    elif intent == "GET_TIME":
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    # Date
    elif intent == "GET_DATE":
        current_date = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}.")

    # Weather
    elif intent == "WEATHER":
        city = entities.get("city")

        if city:
            speak(f"Checking the weather in {city}.")
            weather_result = get_weather(city)
            speak(weather_result)

        else:
            speak("Which city would you like the weather for?")

    # Web search
    elif intent == "WEB_SEARCH":
        search_query = entities.get("query")

        if search_query:
            speak(f"Searching for {search_query}.")

            webbrowser.open(
                "https://www.google.com/search?q="
                + search_query.replace(" ", "+")
            )

        else:
            speak("What would you like me to search for?")

    # Reminder
    elif intent == "SET_REMINDER":
        seconds = entities.get("seconds")
        message = entities.get("message")

        if seconds is not None and message:
            set_reminder(seconds, message, speak)
            speak("Reminder set successfully.")

        else:
            speak("I couldn't understand the reminder time or message.")

    # Exit
    elif intent == "EXIT":
        speak("Goodbye! Have a nice day.")
        break

    # Unknown command
    else:
        speak("I don't understand that command yet.")