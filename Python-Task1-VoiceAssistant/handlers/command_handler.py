from datetime import datetime
import webbrowser

from intents import detect_intent
from weather import get_weather
from reminders import set_reminder

from services.voice_service import listen, speak
from services.email_service import send_email
from services.email_utils import normalize_email

from conversation import ConversationState


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def is_cancel_command(command):
    """Check whether the user wants to cancel the current operation."""

    cancel_phrases = [
        "cancel",
        "cancel email",
        "cancel weather",
        "cancel it",
        "never mind",
        "nevermind",
        "don't send",
        "do not send",
        "stop"
    ]

    return any(
        phrase in command
        for phrase in cancel_phrases
    )


def is_confirmation(command):
    """Check whether the user confirmed an action."""

    confirmation_phrases = [
        "yes",
        "yes send it",
        "yeah",
        "yeah send it",
        "yep",
        "sure",
        "send it",
        "go ahead",
        "confirm"
    ]

    return any(
        phrase in command
        for phrase in confirmation_phrases
    )


# =========================================================
# WEATHER CONVERSATION
# =========================================================

def handle_weather_conversation(state, command):
    """
    Handle the situation where the assistant is waiting
    for the user to provide a city.
    """

    # User can cancel the weather request
    if is_cancel_command(command):

        speak("Okay. Weather request cancelled.")

        state.clear()

        return

    # Treat the user's response as the city
    city = command.strip()

    if not city:

        speak("Please tell me a city name.")

        return

    state.weather_city = city

    speak(
        f"Checking the weather in {city}."
    )

    weather_result = get_weather(city)

    speak(weather_result)

    # Weather conversation is complete
    state.clear()


# =========================================================
# EMAIL CONVERSATION
# =========================================================

def handle_email_conversation(state):
    """
    Handle the multi-step email conversation.
    """

    # -----------------------------------------------------
    # Recipient
    # -----------------------------------------------------

    if not state.recipient:

        speak(
            "Who would you like to send the email to?"
        )

        recipient = listen()

        if not recipient:

            speak(
                "I couldn't hear the recipient."
            )

            return

        if is_cancel_command(recipient):

            speak(
                "Okay. Email cancelled."
            )

            state.clear()

            return

        state.recipient = normalize_email(
            recipient
        )

    # -----------------------------------------------------
    # Subject
    # -----------------------------------------------------

    if not state.subject:

        speak(
            "What should the subject be?"
        )

        subject = listen()

        if not subject:

            speak(
                "I couldn't hear the subject."
            )

            return

        if is_cancel_command(subject):

            speak(
                "Okay. Email cancelled."
            )

            state.clear()

            return

        state.subject = subject

    # -----------------------------------------------------
    # Message
    # -----------------------------------------------------

    if not state.message:

        speak(
            "What should I say in the email?"
        )

        message = listen()

        if not message:

            speak(
                "I couldn't hear the message."
            )

            return

        if is_cancel_command(message):

            speak(
                "Okay. Email cancelled."
            )

            state.clear()

            return

        state.message = message

    # -----------------------------------------------------
    # Confirmation
    # -----------------------------------------------------

    speak(
        f"You want to send an email to "
        f"{state.recipient} "
        f"with the subject "
        f"{state.subject}. "
        f"Should I send it?"
    )

    state.awaiting_confirmation = True

    confirmation = listen()

    if not confirmation:

        speak(
            "I couldn't hear your response. "
            "Please say yes to send or cancel to cancel."
        )

        return

    confirmation = confirmation.lower().strip()

    # -----------------------------------------------------
    # Cancel
    # -----------------------------------------------------

    if is_cancel_command(confirmation):

        speak(
            "Okay. I cancelled the email."
        )

        state.clear()

        return

    # -----------------------------------------------------
    # Confirm
    # -----------------------------------------------------

    if is_confirmation(confirmation):

        success, result = send_email(
            state.recipient,
            state.subject,
            state.message
        )

        speak(result)

        state.clear()

        return

    # -----------------------------------------------------
    # Unknown confirmation
    # -----------------------------------------------------

    speak(
        "I didn't understand. "
        "Please say yes to send the email, "
        "or say cancel to cancel it."
    )


# =========================================================
# MAIN COMMAND HANDLER
# =========================================================

def handle_command(command, state):
    """
    Process one user command.
    """

    command = command.lower().strip()

    if not command:
        return True

    # =====================================================
    # WEATHER CONVERSATION STATE
    # =====================================================

    if state.is_weather_active():

        handle_weather_conversation(
            state,
            command
        )

        return True

    # =====================================================
    # EMAIL CONVERSATION STATE
    # =====================================================

    if state.is_email_active():

        if is_cancel_command(command):

            speak(
                "Okay. Email cancelled."
            )

            state.clear()

            return True

        handle_email_conversation(state)

        return True

    # =====================================================
    # INTENT DETECTION
    # =====================================================

    result = detect_intent(command)

    intent = result["intent"]
    entities = result["entities"]

    # =====================================================
    # GREETING
    # =====================================================

    if intent == "GREETING":

        speak(
            "Hello! How can I help you?"
        )

    # =====================================================
    # TIME
    # =====================================================

    elif intent == "GET_TIME":

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )

        speak(
            f"The current time is {current_time}."
        )

    # =====================================================
    # DATE
    # =====================================================

    elif intent == "GET_DATE":

        current_date = datetime.now().strftime(
            "%B %d, %Y"
        )

        speak(
            f"Today's date is {current_date}."
        )

    # =====================================================
    # WEATHER
    # =====================================================

    elif intent == "WEATHER":

        city = entities.get("city")

        if city:

            speak(
                f"Checking the weather in {city}."
            )

            weather_result = get_weather(city)

            speak(weather_result)

        else:

            speak(
                "Which city would you like "
                "the weather for?"
            )

            # Tell ConversationState that the next
            # response should be treated as a city.
            state.start_weather()

    # =====================================================
    # WEB SEARCH
    # =====================================================

    elif intent == "WEB_SEARCH":

        search_query = entities.get("query")

        if search_query:

            speak(
                f"Searching for {search_query}."
            )

            url = (
                "https://www.google.com/search?q="
                + search_query.replace(" ", "+")
            )

            webbrowser.open(url)

        else:

            speak(
                "What would you like me to search for?"
            )

    # =====================================================
    # REMINDER
    # =====================================================

    elif intent == "SET_REMINDER":

        seconds = entities.get("seconds")
        message = entities.get("message")

        if seconds is not None and message:

            set_reminder(
                seconds,
                message,
                speak
            )

            speak(
                "Reminder set successfully."
            )

        else:

            speak(
                "I couldn't understand the "
                "reminder time or message."
            )

    # =====================================================
    # EMAIL
    # =====================================================

    elif intent == "SEND_EMAIL":

        state.start_email()

        handle_email_conversation(state)

    # =====================================================
    # EXIT
    # =====================================================

    elif intent == "EXIT":

        speak(
            "Goodbye! Have a nice day."
        )

        return False

    # =====================================================
    # UNKNOWN
    # =====================================================

    else:

        speak(
            "I don't understand that command yet."
        )

    return True