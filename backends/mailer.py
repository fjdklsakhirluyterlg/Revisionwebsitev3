import ssl
import smtplib
from email.message import EmailMessage

def validate_user_with_email_better(address, securitykey, name):
    sender_email = "banerjee.armaan@hotmail.com"
    password = "Transport11."