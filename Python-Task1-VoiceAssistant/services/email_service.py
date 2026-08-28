import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

from services.logger import logger


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# =========================================================
# SEND EMAIL
# =========================================================

def send_email(recipient, subject, message):
    """
    Send an email using the configured SMTP account.

    Returns:
        tuple:
            (True, success message)
            or
            (False, error message)
    """

    # -----------------------------------------------------
    # Configuration check
    # -----------------------------------------------------

    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:

        logger.error(
            "Email configuration is missing."
        )

        return (
            False,
            "Email service is not configured."
        )

    # -----------------------------------------------------
    # Input validation
    # -----------------------------------------------------

    if not recipient:
        logger.warning(
            "Email sending requested without recipient."
        )

        return (
            False,
            "Recipient email address is required."
        )

    if not subject:
        logger.warning(
            "Email sending requested without subject."
        )

        return (
            False,
            "Email subject is required."
        )

    if not message:
        logger.warning(
            "Email sending requested without message."
        )

        return (
            False,
            "Email message is required."
        )

    try:

        # -------------------------------------------------
        # Create email
        # -------------------------------------------------

        email = EmailMessage()

        email["From"] = EMAIL_ADDRESS
        email["To"] = recipient
        email["Subject"] = subject

        email.set_content(message)

        # -------------------------------------------------
        # Connect to Gmail SMTP
        # -------------------------------------------------

        with smtplib.SMTP(
            "smtp.gmail.com",
            587,
            timeout=10
        ) as server:

            server.starttls()

            server.login(
                EMAIL_ADDRESS,
                EMAIL_PASSWORD
            )

            server.send_message(email)

        logger.info(
            f"Email sent successfully to: {recipient}"
        )

        return (
            True,
            "Email sent successfully."
        )

    # -----------------------------------------------------
    # Authentication error
    # -----------------------------------------------------

    except smtplib.SMTPAuthenticationError:

        logger.error(
            "Email authentication failed."
        )

        return (
            False,
            "Email authentication failed. "
            "Please check your email credentials "
            "and app password."
        )

    # -----------------------------------------------------
    # Invalid recipient / SMTP error
    # -----------------------------------------------------

    except smtplib.SMTPRecipientsRefused:

        logger.error(
            f"Email recipient was refused: {recipient}"
        )

        return (
            False,
            "The recipient email address was rejected."
        )

    except smtplib.SMTPException as error:

        logger.error(
            f"SMTP error while sending email: {error}"
        )

        return (
            False,
            "There was a problem sending the email."
        )

    # -----------------------------------------------------
    # Network error
    # -----------------------------------------------------

    except OSError as error:

        logger.error(
            f"Email connection error: {error}"
        )

        return (
            False,
            "I couldn't connect to the email server."
        )

    # -----------------------------------------------------
    # Unexpected error
    # -----------------------------------------------------

    except Exception as error:

        logger.exception(
            f"Unexpected email error: {error}"
        )

        return (
            False,
            "Something went wrong while sending the email."
        )