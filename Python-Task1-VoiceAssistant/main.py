from datetime import datetime
import webbrowser

from intents import detect_intent
from weather import get_weather
from reminders import set_reminder

from services.voice_service import listen, speak
from services.email_service import send_email
from services.email_utils import normalize_email
from services.qa_service import answer_question
from services.command_service import find_custom_command


def is_cancel_command(command):
    """
    Check whether the user wants to cancel an operation.
    """

    return any(
        phrase in command
        for phrase in [
            "cancel",
            "cancel email",
            "cancel it",
            "never mind",
            "nevermind",
            "don't send",
            "do not send"
        ]
    )


while True:

    command = listen()

    if not command:
        continue

    result = detect_intent(command)

    intent = result["intent"]
    entities = result["entities"]

    # =====================================================
    # CUSTOM COMMAND
    # =====================================================

    custom_command = find_custom_command(command)

    if custom_command:

        action = custom_command.get("action")

        if action:

            speak(
                f"Opening {custom_command.get('name')}."
            )

            try:

                webbrowser.open(action)

            except Exception as error:

                print(
                    f"Custom command error: {error}"
                )

                speak(
                    "I couldn't execute that custom command."
                )

        else:

            speak(
                "The custom command has no action configured."
            )

        continue

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

            weather_result = get_weather(
                city
            )

            speak(
                weather_result
            )

        else:

            speak(
                "Which city would you like the weather for?"
            )

            city = listen()

            if city:

                speak(
                    f"Checking the weather in {city}."
                )

                weather_result = get_weather(
                    city
                )

                speak(
                    weather_result
                )

            else:

                speak(
                    "I couldn't get the city name."
                )

    # =====================================================
    # GENERAL Q&A
    # =====================================================

    elif intent == "GENERAL_QA":

        question = entities.get(
            "question"
        )

        if question:

            speak(
                "Let me find the answer."
            )

            answer = answer_question(
                question
            )

            speak(
                answer
            )

        else:

            speak(
                "What would you like to know?"
            )

    # =====================================================
    # WEB SEARCH
    # =====================================================

    elif intent == "WEB_SEARCH":

        search_query = entities.get(
            "query"
        )

        if search_query:

            speak(
                f"Searching for {search_query}."
            )

            webbrowser.open(
                "https://www.google.com/search?q="
                + search_query.replace(
                    " ",
                    "+"
                )
            )

        else:

            speak(
                "What would you like me to search for?"
            )

    # =====================================================
    # REMINDER
    # =====================================================

    elif intent == "SET_REMINDER":

        seconds = entities.get(
            "seconds"
        )

        message = entities.get(
            "message"
        )

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
                "I couldn't understand the reminder "
                "time or message."
            )

    # =====================================================
    # EMAIL
    # =====================================================

    elif intent == "SEND_EMAIL":

        recipient = entities.get(
            "recipient"
        )

        subject = entities.get(
            "subject"
        )

        message = entities.get(
            "message"
        )

        # -------------------------------------------------
        # Recipient
        # -------------------------------------------------

        if not recipient:

            speak(
                "Who would you like to send the email to?"
            )

            recipient = listen()

            if is_cancel_command(recipient):

                speak(
                    "Okay. Email cancelled."
                )

                continue

        recipient = normalize_email(
            recipient
        )

        # -------------------------------------------------
        # Subject
        # -------------------------------------------------

        if not subject:

            speak(
                "What should the subject be?"
            )

            subject = listen()

            if is_cancel_command(subject):

                speak(
                    "Okay. Email cancelled."
                )

                continue

        # -------------------------------------------------
        # Message
        # -------------------------------------------------

        if not message:

            speak(
                "What should I say in the email?"
            )

            message = listen()

            if is_cancel_command(message):

                speak(
                    "Okay. Email cancelled."
                )

                continue

        # -------------------------------------------------
        # Validate details
        # -------------------------------------------------

        if recipient and subject and message:

            speak(
                f"You want to send an email to "
                f"{recipient} with the subject "
                f"{subject}. Should I send it?"
            )

            confirmation = listen()

            # -------------------------------------------------
            # Confirm
            # -------------------------------------------------

            if any(
                phrase in confirmation
                for phrase in [
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
            ):

                success, email_result = send_email(
                    recipient,
                    subject,
                    message
                )

                speak(
                    email_result
                )

            # -------------------------------------------------
            # Cancel
            # -------------------------------------------------

            elif is_cancel_command(
                confirmation
            ) or any(
                phrase in confirmation
                for phrase in [
                    "no",
                    "no don't send",
                    "no do not send"
                ]
            ):

                speak(
                    "Okay. I cancelled the email."
                )

            # -------------------------------------------------
            # Unknown confirmation
            # -------------------------------------------------

            else:

                speak(
                    "I didn't understand. "
                    "Please say yes to send the email, "
                    "or say cancel to cancel it."
                )

        else:

            speak(
                "I couldn't get all the email details."
            )

    # =====================================================
    # EXIT
    # =====================================================

    elif intent == "EXIT":

        speak(
            "Goodbye! Have a nice day."
        )

        break

    # =====================================================
    # UNKNOWN
    # =====================================================

    else:

        speak(
            "I don't understand that command yet."
        )