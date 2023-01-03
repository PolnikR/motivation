# This is a sample Python script.
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import App
import smtplib, ssl
from email.message import EmailMessage


obj = App.WebScrapper()
obj2 = App.EmailSender()

l=obj.getAllQuotes()
print(l[1].text)

obj2.sendEmail(obj.getAllQuotes()[5].text)
