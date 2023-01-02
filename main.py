# This is a sample Python script.
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import App
import smtplib, ssl
from email.message import EmailMessage


obj = App.WebScrapper()

email_sender = 'polnikr@gmail.com'
email_password = "umlghoocrwlsltny"

email_receiver = 'ochotnicky.simon1@gmail.com'

subject = "Dont"
body = "abcs"


def send_email(self, to_email, message):
    msg = EmailMessage()
    msg['Subject'] = 'Motivational Quote'
    msg['From'] = self.email
    msg['To'] = to_email
    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(self.email, self.password)
        smtp.send_message(msg)


send_email()
