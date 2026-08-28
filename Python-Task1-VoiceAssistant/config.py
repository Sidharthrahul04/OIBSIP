import os
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# Weather API
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


# Email configuration
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def validate_config():
    """Check whether required configuration values exist."""

    missing = []

    if not WEATHER_API_KEY:
        missing.append("WEATHER_API_KEY")

    if not EMAIL_ADDRESS:
        missing.append("EMAIL_ADDRESS")

    if not EMAIL_PASSWORD:
        missing.append("EMAIL_PASSWORD")

    if missing:
        raise RuntimeError(
            "Missing configuration values: "
            + ", ".join(missing)
        )