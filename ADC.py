from tkinter import *
from tkinter import messagebox
import os
import pandas as pd

def new_file():
    a = open("data.txt", "x")
    a.close()
    
    header = f'{"Firstname"},{"Lastname"},{"City"}\n'
    aa = open("data.txt", "w")
    aa.write(header)
    aa.close()
    messagebox.showinfo("showinfo","File is created")

def apend_data():
    first_name = entry.get()
    last_name = entry2.get()
    city = entry3.get()

    data = pd.DataFrame({"Firstname": [first_name],
                         "Lastname": [last_name],
                         "City": [city]})
    
    data.to_csv("data.txt", mode="a", index=False, header= False)
    messagebox.showinfo("showinfo","File is updated")

def clear():
    entry.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

def delete_file():
    os.remove("data.txt")
    messagebox.showinfo("showinfo","The file has been deleted")

def focus_next_entry(event):
    event.widget.tk_focusNext().focus()
    return "break"

window = Tk()
window.geometry("425x175")
window.title("Automate Data Collector")
icon = PhotoImage(file="C:\\Users\\123\\AppData\\Local\\Programs\\Python\\Python311\\PythonProjects\\ADC\\logo.png")
window.iconphoto(True, icon)
window.config(background="skyblue")

label = Label(window, text="Firstname: ", font=("Arial", 18, "bold"), fg="green", bg="skyblue").place(x=0,y=0)
label2 = Label(window,text="Lastname: ", font=("Arial",18,"bold"),fg="green", bg="skyblue").place(x=0, y=35)
label3 = Label(window,text="State: ", font=("Arial",18,"bold"), fg="green", bg="skyblue").place(x=0, y=75)

entry = Entry(window, font=("Arial", 18), fg="black", bg="white")
entry2 = Entry(window, font=("Arial", 18), fg="black", bg="white")
entry3 = Entry(window, font=("Arial", 18), fg="black", bg="white")

entry.place(x=140, y=5)
entry2.place(x=140, y=40)
entry3.place(x=140, y=75)

button = Button(window, text="New", font=("arial",10,"bold"), fg="white", bg="blue", command=new_file).place(x=75, y=120)
button2 = Button(window, text="Update", font=("arial",10,"bold"), fg="white", bg="blue", command=apend_data).place(x=120, y=120)
button3 = Button(window, text="Clear", font=("arial",10,"bold"), fg="white", bg="blue", command=clear).place(x=183, y=120)
button4 = Button(window, text="Delete File", font=("Arial",10,"bold"), fg="white", bg="blue", command=delete_file).place(x=235, y=120)

entry.bind("<Return>", focus_next_entry)
entry2.bind("<Return>", focus_next_entry)
entry3.bind("<Return>", focus_next_entry)

window.mainloop()
