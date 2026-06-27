from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root=Tk()
root.title=("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

upload=Image.open("")
upload=upload.resize((300,300))
image=ImageTk.Photoimage(upload)

label=Label(root,image=image,bg="light blue")
label.place(x=180,y=20)

label1=Label(
    root,
    text="Hello Sir. Welcome to Denomination Counter Appliication",
    bg="light blue"
)
label1.place(relx=0.5,y=340,anchor=CENTER)

def msg():
    MsgBox=messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    )
    if MsgBox=="ok":
        topwin()

button1=Button(
    root,
    text="Let us get started.",
    command=msg,
    bg="brown"
    fg="white"
)
button1.place(x=260,y=360)