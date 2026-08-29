import re


def normalize_email(text):
    """
    Convert common speech-recognition representations
    of an email address into a standard email format.
    """

    if not text:
        return ""

    text = text.lower().strip()

    # ---------------------------------------------
    # Spoken email symbols
    # ---------------------------------------------

    replacements = {
        " at the rate ": "@",
        " at rate ": "@",
        " at ": "@",
        " dot ": ".",
        " underscore ": "_",
        " hyphen ": "-",
        " dash ": "-"
    }

    for spoken, symbol in replacements.items():
        text = text.replace(spoken, symbol)

    # ---------------------------------------------
    # Remove spaces around @ and .
    # ---------------------------------------------

    text = re.sub(r"\s*@\s*", "@", text)

    text = re.sub(r"\s*\.\s*", ".", text)

    # ---------------------------------------------
    # Remove spaces from email local part
    #
    # voice assistant 96@gmail.com
    # →
    # voiceassistant96@gmail.com
    # ---------------------------------------------

    if "@" in text:

        local_part, domain = text.split("@", 1)

        local_part = re.sub(
            r"\s+",
            "",
            local_part
        )

        domain = re.sub(
            r"\s+",
            "",
            domain
        )

        text = f"{local_part}@{domain}"

    return text


def is_valid_email(email):
    """
    Check whether an email address has a valid
    basic email structure.
    """

    if not email:
        return False

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return bool(
        re.match(pattern, email)
    )