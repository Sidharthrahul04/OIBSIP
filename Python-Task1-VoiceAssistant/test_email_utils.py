from services.email_utils import (
    normalize_email,
    is_valid_email
)


test_emails = [
    "voice assistant 96 at gmail dot com",
    "voiceassistant96@gmail.com",
    "john dot doe at gmail dot com",
    "test at outlook dot com",
    "invalid email"
]


for email in test_emails:

    normalized = normalize_email(email)

    valid = is_valid_email(normalized)

    print("\nOriginal:", email)
    print("Normalized:", normalized)
    print("Valid:", valid)