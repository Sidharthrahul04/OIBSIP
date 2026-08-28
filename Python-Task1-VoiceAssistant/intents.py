import re


# =========================================================
# CITY EXTRACTION
# =========================================================

def extract_city(command):

    patterns = [
        r"(?:weather|temperature)\s+(?:in|at|for)\s+(.+)",
        r"(?:weather|temperature)\s+(?:of)\s+(.+)",
        r"(?:weather|temperature)\s+(?:like)\s+(?:in|at|for)\s+(.+)",
        r"how(?:'s| is)\s+the\s+(?:weather|temperature)\s+(?:in|at|for)\s+(.+)",
        r"how\s+is\s+(.+?)\s+(?:weather|temperature)",
        r"what(?:'s| is)\s+the\s+(?:weather|temperature)\s+(?:in|at|for)\s+(.+)",
    ]

    for pattern in patterns:

        match = re.search(pattern, command)

        if match:

            city = match.group(1).strip()

            city = re.sub(
                r"\s+(today|now|currently|right now)$",
                "",
                city
            ).strip()

            if city:
                return city

    return None


# =========================================================
# REMINDER DETAILS EXTRACTION
# =========================================================

def extract_reminder_details(command):

    patterns = [
        (
            r"remind me (?:in )?(\d+)\s+seconds?\s+to\s+(.+)",
            1
        ),
        (
            r"remind me (?:in )?(\d+)\s+minutes?\s+to\s+(.+)",
            60
        ),
        (
            r"remind me (?:in )?(\d+)\s+hours?\s+to\s+(.+)",
            3600
        ),
    ]

    for pattern, multiplier in patterns:

        match = re.search(pattern, command)

        if match:

            amount = int(match.group(1))
            message = match.group(2).strip()

            seconds = amount * multiplier

            return seconds, message

    return None, None


# =========================================================
# WEB SEARCH QUERY EXTRACTION
# =========================================================

def extract_search_query(command):

    search_patterns = [
        r"^search (.+)",
        r"^search for (.+)",
        r"^please search (.+)",
        r"^please search for (.+)",
        r"^can you search (.+)",
        r"^can you search for (.+)",
        r"^could you search (.+)",
        r"^could you search for (.+)",
        r"^look up (.+)",
        r"^find information about (.+)",
        r"^google (.+)"
    ]

    for pattern in search_patterns:

        match = re.search(pattern, command)

        if match:

            query = match.group(1).strip()

            if query:
                return query

    return None


# =========================================================
# INTENT DETECTION
# =========================================================

def detect_intent(command):

    command = command.lower().strip()

    # =====================================================
    # EMPTY COMMAND
    # =====================================================

    if not command:

        return {
            "intent": "UNKNOWN",
            "entities": {}
        }

    # =====================================================
    # REMINDER
    # =====================================================

    if "remind me" in command:

        seconds, message = extract_reminder_details(command)

        return {
            "intent": "SET_REMINDER",
            "entities": {
                "seconds": seconds,
                "message": message
            }
        }

    # =====================================================
    # WEATHER
    # =====================================================

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

    # =====================================================
    # EMAIL
    # =====================================================

    if any(phrase in command for phrase in [
        "send an email",
        "send email",
        "compose an email",
        "compose email",
        "write an email",
        "write email"
    ]):

        return {
            "intent": "SEND_EMAIL",
            "entities": {}
        }

    # =====================================================
    # GREETING
    # =====================================================

    if re.search(
        r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b",
        command
    ):

        return {
            "intent": "GREETING",
            "entities": {}
        }

    # =====================================================
    # TIME
    # =====================================================

    if (
        "time" in command
        and any(word in command for word in [
            "what",
            "tell",
            "current",
            "know",
            "give"
        ])
    ):

        return {
            "intent": "GET_TIME",
            "entities": {}
        }

    # =====================================================
    # DATE
    # =====================================================

    if (
        "date" in command
        and any(word in command for word in [
            "what",
            "today",
            "current",
            "tell",
            "know"
        ])
    ):

        return {
            "intent": "GET_DATE",
            "entities": {}
        }

    # =====================================================
    # GENERAL Q&A
    # =====================================================

    if any(phrase in command for phrase in [
        "who is",
        "who was",
        "who invented",
        "what is",
        "what are",
        "where is",
        "when was",
        "when did",
        "why is",
        "how does",
        "how do",
        "how is",
        "tell me about",
        "can you tell me about",
        "can you tell me"
    ]):

        return {
            "intent": "GENERAL_QA",
            "entities": {
                "question": command
            }
        }

    # =====================================================
    # WEB SEARCH
    # =====================================================

    search_query = extract_search_query(command)

    if search_query:

        return {
            "intent": "WEB_SEARCH",
            "entities": {
                "query": search_query
            }
        }

    # =====================================================
    # EXIT
    # =====================================================

    if any(phrase in command for phrase in [
        "exit",
        "quit",
        "goodbye",
        "good bye",
        "close assistant",
        "stop assistant"
    ]):

        return {
            "intent": "EXIT",
            "entities": {}
        }

    # =====================================================
    # UNKNOWN
    # =====================================================

    return {
        "intent": "UNKNOWN",
        "entities": {}
    }