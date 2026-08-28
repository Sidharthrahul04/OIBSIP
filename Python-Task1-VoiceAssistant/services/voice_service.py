import speech_recognition as sr
import pyttsx3

from services.logger import logger


# =========================================================
# SPEECH RECOGNIZER
# =========================================================

recognizer = sr.Recognizer()


# =========================================================
# TEXT-TO-SPEECH
# =========================================================

def speak(text):
    """
    Convert text into speech and display the response
    in the terminal.
    """

    print(f"Assistant: {text}")

    try:

        engine = pyttsx3.init()

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as error:

        logger.error(
            f"TTS error: {error}"
        )

        print(
            f"TTS error: {error}"
        )


# =========================================================
# SPEECH-TO-TEXT
# =========================================================

def listen():
    """
    Capture voice from the microphone and convert it
    into text.

    Returns:
        str: Recognized text or an empty string if
             recognition fails.
    """

    # =====================================================
    # MICROPHONE INPUT
    # =====================================================

    try:

        with sr.Microphone() as source:

            print("Listening...")

            # Adjust to background noise
            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            # Listen for the user's voice
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

    # -----------------------------------------------------
    # No speech detected
    # -----------------------------------------------------

    except sr.WaitTimeoutError:

        logger.warning(
            "No speech detected within timeout."
        )

        speak(
            "I didn't hear anything. "
            "Please try again."
        )

        return ""

    # -----------------------------------------------------
    # Microphone unavailable
    # -----------------------------------------------------

    except OSError as error:

        logger.error(
            f"Microphone access error: {error}"
        )

        speak(
            "I couldn't access the microphone. "
            "Please check your microphone."
        )

        return ""

    # -----------------------------------------------------
    # Other microphone errors
    # -----------------------------------------------------

    except Exception as error:

        logger.error(
            f"Unexpected microphone error: {error}"
        )

        print(
            f"Microphone error: {error}"
        )

        speak(
            "There was a problem with the microphone."
        )

        return ""

    # =====================================================
    # SPEECH RECOGNITION
    # =====================================================

    try:

        # Convert captured audio into text
        text = recognizer.recognize_google(
            audio
        )

        print(
            f"You said: {text}"
        )

        logger.info(
            f"Speech recognized: {text}"
        )

        return text.lower().strip()

    # -----------------------------------------------------
    # Speech could not be understood
    # -----------------------------------------------------

    except sr.UnknownValueError:

        logger.warning(
            "Speech could not be understood."
        )

        speak(
            "Sorry, I couldn't understand you. "
            "Please repeat that."
        )

        return ""

    # -----------------------------------------------------
    # Google Speech Recognition unavailable
    # -----------------------------------------------------

    except sr.RequestError as error:

        logger.error(
            f"Speech recognition service error: {error}"
        )

        speak(
            "The speech recognition service is "
            "currently unavailable."
        )

        return ""

    # -----------------------------------------------------
    # Unexpected speech-recognition error
    # -----------------------------------------------------

    except Exception as error:

        logger.error(
            f"Unexpected speech recognition error: {error}"
        )

        print(
            f"Speech recognition error: {error}"
        )

        speak(
            "There was a problem processing your speech."
        )

        return ""