import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser


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

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    elif "date" in command:
        current_date = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}.")

    elif "search" in command:
        search_query = command.replace("search", "", 1).strip()

        if search_query:
            speak(f"Searching for {search_query}.")
            webbrowser.open(
                "https://www.google.com/search?q="
                + search_query.replace(" ", "+")
            )
        else:
            speak("What would you like me to search for?")

    elif "exit" in command or "quit" in command or "goodbye" in command:
        speak("Goodbye! Have a nice day.")
        break

    elif command:
        speak("I don't understand that command yet.")