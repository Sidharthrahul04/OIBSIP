import os
import smtplib

from email.message import EmailMessage

from services.logger import logger
from services.email_utils import (
    normalize_email,
    is_valid_email
)


def send_email(recipient, subject, message):
    """
    Send an email using Gmail SMTP.
    """

    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:

        logger.error(
            "Email configuration is missing."
        )

        return (
            False,
            "Email configuration is missing."
        )

    # ---------------------------------------------
    # Normalize recipient
    # ---------------------------------------------

    recipient = normalize_email(recipient)

    # ---------------------------------------------
    # Validate recipient
    # ---------------------------------------------

    if not is_valid_email(recipient):

        logger.warning(
            f"Invalid recipient email: {recipient}"
        )

        return (
            False,
            f"The email address {recipient} is not valid."
        )

    try:

        email = EmailMessage()

        email["From"] = sender_email
        email["To"] = recipient
        email["Subject"] = subject

        email.set_content(message)

        # -----------------------------------------
        # Connect to Gmail SMTP
        # -----------------------------------------

        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as server:

            server.starttls()

            server.login(
                sender_email,
                sender_password
            )

            server.send_message(email)

        logger.info(
            f"Email sent successfully to: {recipient}"
        )

        return (
            True,
            "Email sent successfully."
        )

    except smtplib.SMTPAuthenticationError as error:

        logger.error(
            f"Email authentication failed: {error}"
        )

        return (
            False,
            "Email authentication failed. "
            "Please check your Gmail app password."
        )

    except smtplib.SMTPException as error:

        logger.error(
            f"SMTP error: {error}"
        )

        return (
            False,
            "I couldn't send the email."
        )

    except Exception as error:

        logger.exception(
            f"Unexpected email error: {error}"
        )

        return (
            False,
            "Something went wrong while sending the email."
        )