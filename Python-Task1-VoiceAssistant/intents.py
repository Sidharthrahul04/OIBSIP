import re


def extract_city(command):
    patterns = [
        r"weather in (.+)",
        r"weather at (.+)",
        r"weather for (.+)",
        r"temperature in (.+)",
        r"temperature at (.+)",
        r"temperature for (.+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, command)

        if match:
            city = match.group(1).strip()
            return city

    return None

def extract_reminder_details(command):
    patterns = [
        r"remind me (?:in )?(\d+) seconds? to (.+)",
        r"remind me (?:in )?(\d+) minutes? to (.+)",
        r"remind me (?:in )?(\d+) hours? to (.+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, command)

        if match:
            amount = int(match.group(1))
            message = match.group(2).strip()

            if "second" in pattern:
                seconds = amount

            elif "minute" in pattern:
                seconds = amount * 60

            else:
                seconds = amount * 3600

            return seconds, message

    return None, None
def detect_intent(command):
    command = command.lower().strip()

        # Reminder
    if "remind me" in command:
        seconds, message = extract_reminder_details(command)

        return {
            "intent": "SET_REMINDER",
            "entities": {
                "seconds": seconds,
                "message": message
            }
        }

     # Weather
    if any(word in command for word in [
            "weather",
            "temperature"
        ]):
            city = extract_city(command)
    
            return {
                "intent": "WEATHER",
                "entities": {
                    "city": city
                }
            }
    
    # Greeting
    if re.search(r"\b(hello|hi|hey)\b", command):
        return {
            "intent": "GREETING",
            "entities": {}
        }

    # Time
    if "time" in command and any(word in command for word in [
        "what",
        "tell",
        "current",
        "know"
    ]):
        return {
            "intent": "GET_TIME",
            "entities": {}
        }

    # Date
    if any(phrase in command for phrase in [
        "what date",
        "today's date",
        "todays date",
        "current date",
        "date today"
    ]):
        return {
            "intent": "GET_DATE",
            "entities": {}
        }

   
    # Web search
    if command.startswith("search "):
        search_query = command.replace("search", "", 1).strip()

        return {
            "intent": "WEB_SEARCH",
            "entities": {
                "query": search_query
            }
        }

    # Exit
    if any(word in command for word in [
        "exit",
        "quit",
        "goodbye"
    ]):
        return {
            "intent": "EXIT",
            "entities": {}
        }

    return {
        "intent": "UNKNOWN",
        "entities": {}
    }