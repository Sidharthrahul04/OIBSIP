from services.email_utils import normalize_email, is_valid_email


test_emails = [
    "voiceassistant96@gmail.com",
    "voice assistant 96@gmail.com",
    "voice assistant 96 at gmail dot com",
    "john at gmail dot com",
    "test underscore user at gmail dot com"
]


for email in test_emails:

    normalized = normalize_email(email)

    print(f"Original:   {email}")
    print(f"Normalized: {normalized}")
    print(f"Valid:      {is_valid_email(normalized)}")
    print()