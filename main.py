import tkinter as tk
from tkinter import messagebox
import App
import random

obj = App.WebScrapper()
obj2 = App.EmailSender()
obj3 = App.SmsSender()
obj4 = App.SharePointListUpload()

list_name = obj.get_all_quotes()

root = tk.Tk()
root.title("Motivation quotes")
root.geometry("800x500")


def next_button_click(lst):
    global number
    number = random.randint(0, len(lst))



button = tk.Button(root, text="Next", command=next_button_click)

label = tk.Label(root, text="Motivation")
label.pack()

button.pack()

root.mainloop()
