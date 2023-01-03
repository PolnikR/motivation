from random import random
import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.message import EmailMessage
from twilio.rest import Client
from shareplum import Site
from shareplum import Office365


class WebScrapper(object):

    def __init__(self, url="https://www.brainyquote.com/topics/motivation"):

        resp = requests.get(url)

        self.soup = BeautifulSoup(resp.text, 'html.parser')

    def get_all_quotes(self):

        return self.soup.find_all("a", {"title": "view quote"})


class EmailSender(object):

    def __init__(self):
        self.email_sender = 'polnikr@gmail.com'
        self.email_password = ''
        self.email_receiver = "roman.polnik@azet.sk"

    def send_email(self, quote):

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
        self.token = ''
        self.fromNumber = '+13853757646'

    def send_sms(self, quote, phone_number):
        cl = Client(self.SID, self.token)
        cl.messages.create(body=quote, from_=self.fromNumber, to=phone_number)


class SharePointListUpload(object):

    def __init__(self):
        self.auth_cookie = Office365('https://servisac.sharepoint.com', username='simon.ochotnicky@esas.autocont.sk', password='Heslo123').GetCookies()
        self.site = Site('https://servisac.sharepoint.com/sites/dev01', authcookie=self.auth_cookie)

    def upload_data(self, list_name, quote):
        new_list = self.site.List(list_name)
        my_data = [{'Title': quote}]
        new_list.update_list_items(data=my_data, kind='New')
