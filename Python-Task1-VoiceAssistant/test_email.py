from services.email_service import send_email


recipient = input("Recipient email: ")
subject = input("Subject: ")
body = input("Message: ")


success, result = send_email(
    recipient,
    subject,
    body
)


print(result)