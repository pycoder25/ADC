from tkinter import *
import pandas as pd

'''The name of this program is Automate Data Collector(ADC)'''
'Creator: Diego Lopez'
'Date: 10/05/2023'


def save_data():
    first_name = entry.get()
    last_name = entry2.get()
    city = entry3.get()

    data = pd.DataFrame({"First Name": [first_name],
                         "Last Name": [last_name],
                         "City": [city]})
    data.to_csv("data.csv", index=False)


def apend_data():
    first_name = entry.get()
    last_name = entry2.get()
    city = entry3.get()

    data = pd.DataFrame({"First Name": [first_name],
                         "Last Name": [last_name],
                         "City": [city]})

   
    data.to_csv("data.csv", mode='a', index=False, header=False)



def delete_data():
    entry.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

def focus_next_entry(event):
    event.widget.tk_focusNext().focus()
    return "break"

window = Tk()
window.geometry("500x375")
window.title("Personal Detail")
window.config(background="black")

title = Label(window, text="Fill up the empty fields",
              font=("Arial", 25, "bold"),
              fg="blue",
              bg="black")
title.grid(row=0, column=0, columnspan=2)

label = Label(window, text="First name: ", font=("Arial", 18, "bold"), fg="green", bg="black")
label2 = Label(window,text="Last name: ", font=("Arial",18,"bold"),fg="green", bg="black")
label3 = Label(window,text="State: ", font=("Arial",18,"bold"), fg="green", bg="black")
entry = Entry(window, font=("Arial", 18), fg="black", bg="orange")
entry2 = Entry(window, font=("Arial", 18), fg="black", bg="orange")
entry3 = Entry(window, font=("Arial", 18), fg="black", bg="orange")
button = Button(window, text="New Data", font=("arial",10,"bold"), fg="white", bg="blue",command=save_data)
button2 = Button(window, text="Append Data", font=("arial",10,"bold"), fg="white", bg="blue",command=apend_data)
button3 = Button(window, text="Delete Data", font=("arial",10,"bold"), fg="white", bg="blue",command=delete_data)

label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
label2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
label3.grid(row=3, column=0, sticky="w", padx=10, pady=10)
entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)
entry2.grid(row=2, column=1, sticky="w", padx=10, pady=10)
entry3.grid(row=3, column=1, sticky="w", padx=10, pady=10)
button.grid(row=4, column=0, columnspan=1, padx=10, pady=10)
button2.grid(row=5, column=0, columnspan=1, padx=10, pady=10)
button3.grid(row=6, column=0, columnspan=1, padx=10, pady=10)

entry.bind("<Return>", focus_next_entry)
entry2.bind("<Return>", focus_next_entry)
entry3.bind("<Return>", focus_next_entry)

window.mainloop()