# from email.MIMEMultipart import MIMEMultipart
import random
from email.mime.text import MIMEText
import email
import json
import os
from queue import Queue
import smtplib
import time


from logger import logger
from enums import EnvironmentVariable
import constant

emails = Queue()


class StratoMailClient:
    def __init__(self, username: str, password: str, sender_address: str):
        logger.info(msg="Initializing mail client...")
        self.host = "smtp.strato.de"
        self.port = "465"
        self.username = username
        self.password = password
        self.sender_address = sender_address
        logger.info(msg="Mail client intialized.")

    def send_mail(self, receiver_address: str, subject: str, message: str):
        logger.info(msg="Sending email...")
        msg = MIMEText(message.encode("utf-8"), _charset="utf-8")
        msg["To"] = email.utils.formataddr(("Recipient", receiver_address))
        msg["From"] = email.utils.formataddr(("Author", self.sender_address))
        msg["Subject"] = subject
        try:
            with smtplib.SMTP_SSL(f"{self.host}:{self.port}") as server:
                server.login(self.username, self.password)
                server.sendmail(
                    self.sender_address, [receiver_address], msg.as_string()
                )
                server.quit()
        except Exception as e:
            logger.info(msg=f"Failed to send email. {e}")
        else:
            logger.info(msg="Email successfully sent.")


def generate_email():
    logger.info("New mail will be generated...")
    with open(constant.config_path / "content.json", "r", encoding="utf-8") as file:
        content = json.loads(file.read())
    recipient = content["email"]
    subject = random.choice(content["subjects"])
    message = (
        random.choice(content["greetings"]) + "\n" + random.choice(content["bodies"])
    )
    logger.info("Mail has been generated.")
    push_new_email(receiver_address=recipient, subject=subject, message=message)


def push_new_email(receiver_address: str, subject: str, message: str):
    logger.info("Attaching new mail to the queue...")
    emails.put({"receiver": receiver_address, "subject": subject, "message": message})
    logger.info("New mail attached to the queue.")


def run_mails():
    email_client = StratoMailClient(
        username=os.getenv(EnvironmentVariable.EMAIL_USERNAME_STRATO),
        password=os.getenv(EnvironmentVariable.EMAIL_PASSWORD_STRATO),
        sender_address=os.getenv(EnvironmentVariable.EMAIL_SENDER_ADDRESS),
    )
    while True:
        logger.debug(msg="Checking for new mails in queue...")
        try:
            mail = emails.get(block=False)
        except Exception as e:
            logger.debug(msg="No new mail to send.")
        else:
            logger.info(msg="New mail detected.")
            email_client.send_mail(
                receiver_address=mail["receiver"],
                subject=mail["subject"],
                message=mail["message"],
            )

        time.sleep(1)
