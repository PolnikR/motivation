from random import random
import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.message import EmailMessage


class WebScrapper(object):

    global x
    x=64
    def __init__(self, url="https://www.brainyquote.com/topics/motivation"):

        resp = requests.get(url)

        self.soup = BeautifulSoup(resp.text, 'html.parser')



    def getAllQuotes(self):

        l = self.soup.find_all("a", {"title": "view quote"})
        return l


    def moveNext(self, list):

        if x < len(list):
            x+=1
            print(list[x].text)



class EmailSender(object):

    def __init__(self):
        self.email_sender = 'polnikr@gmail.com'
        self.email_password = ''
        self.email_receiver = "roman.polnik@azet.sk"

    def sendEmail(self):

        subject = "Dont forget to subscribe"
        body = """
        Watch till the end"
        """

        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = self.email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, em.as_string())

class MoveQuote(object):
    def nextQuote(self):
        x=2
