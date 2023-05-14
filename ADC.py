import os
from tkinter import *
from tkinter import messagebox
import pandas as pd

def save_data():
    first_name = entry.get()
    last_name = entry2.get()
    city = entry3.get()

    data = pd.DataFrame({"Firstname": [first_name],
                         "Lastname": [last_name],
                         "City": [city]})
    data.to_csv("data.csv", index=False)
    messagebox.showinfo("The file has been created!")




def apend_data():
    first_name = entry.get()
    last_name = entry2.get()
    city = entry3.get()

    data = pd.DataFrame({"Firstname": [first_name],
                         "Lastname": [last_name],
                         "City": [city]})
    messagebox.showinfo("The file has been updated!")
   
    data.to_csv("data.csv", mode='a', index=False, header=False)
print("The data has been updated!")

def delete_data():
    entry.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

def focus_next_entry(event):
    event.widget.tk_focusNext().focus()
    return "break"

window = Tk()
window.geometry("575x375")
window.title("Personal Detail")
window.config(background="black")

title = Label(window, text="Fill up the empty fields",
              font=("Arial", 25, "bold"),
              fg="blue",
              bg="black")


label = Label(window, text="Firstname: ", font=("Arial", 18, "bold"), fg="green", bg="black")
label2 = Label(window,text="Lastname: ", font=("Arial",18,"bold"),fg="green", bg="black")
label3 = Label(window,text="State: ", font=("Arial",18,"bold"), fg="green", bg="black")
entry = Entry(window, font=("Arial", 18), fg="black", bg="orange")
entry2 = Entry(window, font=("Arial", 18), fg="black", bg="orange")
entry3 = Entry(window, font=("Arial", 18), fg="black", bg="orange")
button = Button(window, text="New", font=("arial",10,"bold"), fg="white", bg="blue",command=save_data)
button2 = Button(window, text="Append", font=("arial",10,"bold"), fg="white", bg="blue",command=apend_data)
button3 = Button(window, text="Delete", font=("arial",10,"bold"), fg="white", bg="blue",command=delete_data)
label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
label2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
label3.grid(row=3, column=0, sticky="w", padx=10, pady=10)
entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)
entry2.grid(row=2, column=1, sticky="w", padx=10, pady=10)
entry3.grid(row=3, column=1, sticky="w", padx=10, pady=10)
button.grid(row=4, column=1, sticky=W, padx=5, pady=5)
button2.grid(row=5, column=1, sticky=W, padx=5, pady=5)
button3.grid(row=6, column=1, sticky=W, padx=5, pady=5)
title.grid(row=0, column=1)
entry.bind("<Return>", focus_next_entry)
entry2.bind("<Return>", focus_next_entry)
entry3.bind("<Return>", focus_next_entry)

window.mainloop()