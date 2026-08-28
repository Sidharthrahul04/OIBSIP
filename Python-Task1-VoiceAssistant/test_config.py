from config import (
    WEATHER_API_KEY,
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    validate_config
)


try:

    validate_config()

    print("Configuration loaded successfully.")

    print(
        "Weather API key:",
        "Loaded" if WEATHER_API_KEY else "Missing"
    )

    print(
        "Email address:",
        EMAIL_ADDRESS if EMAIL_ADDRESS else "Missing"
    )

    print(
        "Email password:",
        "Loaded" if EMAIL_PASSWORD else "Missing"
    )

except RuntimeError as error:

    print("Configuration error:", error)