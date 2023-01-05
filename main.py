import tkinter as tk
from tkinter import messagebox
import App
import random

obj = App.WebScrapper()
obj2 = App.EmailSender()
obj3 = App.SmsSender()
obj4 = App.SharePointListUpload()


list_name = obj.get_all_quotes()
number = random.randint(1, len(list_name)-1)
number1 = number


root = tk.Tk()
root.title("Motivation quotes")
root.geometry("400x650")


def next_button_click():
    global number1
    number1 += 1
    if number1 == len(list_name)-1:
        number1 = 1
    label.config(text=list_name[number1].text)


def previous_button_click():
    global number1
    number1 -= 1
    if number1 >= 1:
        label.config(text=list_name[number1].text)
    else:
        number1 = 1



def send_quote_by_sms():
    obj3.send_sms(list_name[number1].text, '')


def send_quote_by_email():
    obj2.send_email(list_name[number1].text)


def send_quote_to_sharepoint():
    obj4.upload_data("Motivation", list_name[number1].text)


button1 = tk.Button(root, text="Next Quote", height=3, width=20, command=next_button_click, bg="green")
button2 = tk.Button(root, text="Previous Quote", height=3, width=20, command=previous_button_click, bg="green")
button3 = tk.Button(root, text="Send Quote by SMS", height=3, width=20, command=send_quote_by_sms, bg="green")
button4 = tk.Button(root, text="Send Quote by Email", height=3, width=20, command=send_quote_by_email, bg="green")
button5 = tk.Button(root, text="Send Quote to Sharepoint", height=3, width=20, command=send_quote_to_sharepoint, bg="green")
button1.place(x=120,y=175)
button2.place(x=120, y=275)
button3.place(x=120, y=375)
button4.place(x=120, y=475)
button5.place(x=120, y=575)
label = tk.Label(root, text=list_name[number].text, wraplength=350, anchor="n")

label.pack()

root.mainloop()

