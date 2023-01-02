from random import random
import requests
from bs4 import BeautifulSoup
import smtplib, ssl


class WebScrapper(object):

    def __init__(self, url="https://www.brainyquote.com/topics/motivation"):

        resp = requests.get(url)

        self.soup = BeautifulSoup(resp.text, 'html.parser')

    def getAllQuotes(self):

        l = self.soup.find_all("a", {"title": "view quote"})


class EmailSender(object):

    def __init__(self):
        self.sender_email = "polnikr@gmail.com"
        self.receiver_email = "polnikr@gmail.com"
        self.port = 465
        self.password = "25101991"
        self.message = "hello Roman"
        self.server = smtplib.SMTP("smtp.gmail.com",  self.port)

    def sendEmail(self):
        context = ssl.create_default_context()
        #server = smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context)
        self.server.login(self.sender_email, self.password)
        print("logged in")
        #self.server.sendmail(self.sender_email, self.receiver_email, self.message)
