from tkinter import *
from datetime import date

root = Tk()
root.title("Greetings Dashboard")
root.geometry('400x400')

lbl = Label(text="Welcome To Emplpoyee Greetings Dashboard", bg='black', fg='white', height=2, width=300)
name_label = Label(text="Please Enter Full Name", bg='white', fg='black', height=2, width=300) 
name_entry = Entry()

def show():
    name = name_entry.get()
    textbox.delete(1.0,END)
    greeting = 'Hello '+ name +'!'+"\n"
    reported_time = "U Logged into the application at " + str(date.today())

    textbox.insert(END, greeting)
    textbox.insert(END, reported_time)

btn =  Button(text="Log in", command=show,bg="green", fg="black", height=1, width=10)

textbox  = Text(height=5, width=500)
lbl.pack()
name_label.pack()
name_entry.pack()
textbox.pack()
btn.pack()

root.mainloop()