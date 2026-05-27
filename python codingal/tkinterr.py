from tkinter import *
from datetime import date

root=Tk()

root.title("Demo Window")
root.geometry("400x300")

lbl=Label(text="Hey There",fg="white",bg="#072F5F",height=1,width=300)

namelbl=Label(text="Full Name",bg="#3895D3")
nameentry=Entry()


def display():
    name=nameentry.get()
    global message
    message="Welcome to the application.\n Todays date is:"
    greet="Hello "+name+"\n"

    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

text_box=Text(height=3)

btn=Button(text="Begin",command=display,height=1,bg="#1261A0",fg="white")

lbl.pack()
namelbl.pack()
nameentry.pack()
btn.pack()
text_box.pack()

root.mainloop()