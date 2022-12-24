import ssl
import smtplib
from email.message import EmailMessage
from dataclasses import dataclass

def validate_user_with_email_better(address, securitykey, name):
    sender_email = "banerjee.armaan@hotmail.com"
    password = "Transport11."
    subject = "HI there"
    body = f"Hello there, you have been emailed from me, your email adress is {address}"

def user_buy_request(sender, text, reciever):
    pass

@dataclass
class emailer:
    subject: str
    adress: list
    body: str

    def send(self):
        for ad in self.adress:
            message = EmailMessage()
            message["from"] = "banerjee.armaan@hotmail.com"
            message["to"] = ad
            message["subject"] = self.subject
            html = self.body
            message.add_alternative(html, subtype="html")


            context = ssl.create_default_context()




