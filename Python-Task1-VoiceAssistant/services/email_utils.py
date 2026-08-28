import re


def normalize_email(text):
    """
    Convert common speech-recognition representations
    of email addresses into standard email format.
    """

    text = text.lower().strip()

    # Convert spoken email symbols
    text = text.replace(" at ", "@")
    text = text.replace(" dot ", ".")
    text = text.replace(" underscore ", "_")
    text = text.replace(" hyphen ", "-")
    text = text.replace(" dash ", "-")

    # Remove spaces around @
    text = re.sub(r"\s*@\s*", "@", text)

    # Remove spaces around dots
    text = re.sub(r"\s*\.\s*", ".", text)

    # Remove unnecessary spaces inside the email address
    if "@" in text:

        local_part, domain = text.split("@", 1)

        local_part = re.sub(r"\s+", "", local_part)
        domain = re.sub(r"\s+", "", domain)

        text = f"{local_part}@{domain}"

    return text


def is_valid_email(email):
    """
    Perform basic email address validation.
    """

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return re.match(pattern, email) is not None