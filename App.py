from random import random
import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.message import EmailMessage
from twilio.rest import Client


class WebScrapper(object):


    def __init__(self, url="https://www.brainyquote.com/topics/motivation"):

        resp = requests.get(url)

        self.soup = BeautifulSoup(resp.text, 'html.parser')



    def getAllQuotes(self):

        l = self.soup.find_all("a", {"title": "view quote"})
        return l






class EmailSender(object):

    def __init__(self):
        self.email_sender = 'polnikr@gmail.com'
        self.email_password = ''
        self.email_receiver = "roman.polnik@azet.sk"

    def sendEmail(self, quote):

        subject = "Dont forget to subscribe"
        body = quote

        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = self.email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, em.as_string())



class SmsSender(object):

    def __init__(self):
        self.SID = 'AC3310973e3eeba419c573a312ce2ea348'
        self.token = '14de2eb7e612006769db41662ec08c77'
        self.fromNumber = '+13853757646'

    def sendSMS(self, quote, phoneNumber):
        cl = Client(self.SID, self.token)
        cl.messages.create(body=quote, from_=self.fromNumber, to=phoneNumber)
