import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_lead_notification(name, phone):

    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")

    msg = EmailMessage()

    msg["Subject"] = "New Lead Received"
    msg["From"] = email_address
    msg["To"] = email_address

    msg.set_content(
        f"""
New Lead Received

Name: {name}
Phone: {phone}
"""
    )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            email_address,
            email_password
        )

        smtp.send_message(msg)