import tkinter as tk
from tkinter import messagebox
import App
import random

obj = App.WebScrapper()
obj2 = App.EmailSender()
obj3 = App.SmsSender()
obj4 = App.SharePointListUpload()

global number
global number1

list_name = obj.get_all_quotes()
number = random.randint(0, len(list_name))

lst=[]
lst.append(number)

root = tk.Tk()
root.title("Motivation quotes")
root.geometry("400x600")


def next_button_click():
    number1 = random.randint(0, len(list_name))
    if number1==0:
        number1=1
    lst.append(number1)
    label.config(text=list_name[number1].text)

def previous_button_click():
    if len(lst)>1:
        label.config(text=list_name[lst[len(lst)-2]].text)

def send_quote_by_sms():
    obj3.send_sms(list_name[number].text, '+421907474723')


def send_quote_by_email():
    obj2.send_email(list_name[number].text)

def send_quote_to_sharepoint():
    obj4.upload_data("Motivation", list_name[number].text)



button1 = tk.Button(root, text="Next Quote", height=3, width=20, command=next_button_click)
button2 = tk.Button(root, text="Previous Quote", height=3, width=20, command=previous_button_click)
button3 = tk.Button(root, text="Send Quote by SMS", height=3, width=20, command=send_quote_by_sms)
button4 = tk.Button(root, text="Send Quote by Email", height=3, width=20, command=send_quote_by_email)
button5 = tk.Button(root, text="Send Quote to Sharepoint", height=3, width=20, command=send_quote_to_sharepoint)
button1.place(x=120,y=100)
button2.place(x=120, y=200)
button3.place(x=120, y=300)
button4.place(x=120, y=400)
button5.place(x=120, y=500)
label = tk.Label(root, text=list_name[number].text)
label.place(x=0, y=10)
label.pack()

#button1.pack()

root.mainloop()
