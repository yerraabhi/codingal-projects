# from tkinter import *

# window=Tk()
# window.title="Event Handler"
# window.geometry="100x100"

# def handlekeypress(event):
#     """Press the character asscociated to the key pressed"""
#     print(event.char)

# window.bind("<Key>",handlekeypress)

# def handleclick(event):
#     print("\nThe button was clicked")

# button=Button(text="Click Me")
# button.pack()
# button.bind("<Button-1>",handleclick)

# window.mainloop()

# from tkinter import *
# from tkinter import messagebox

# root=Tk()
# root.geometry("400x300")

# def msg():
#     messagebox.showwarning("Alert","Stop. Virus Found")

# button=Button(root, text="Scan For Virus",command=msg)
# button.place(x=40,y=80)

# root.mainloop()

from tkinter import *
from tkinter import messagebox

root=Tk()

response=messagebox.askretrycancel("Connection Error","Unable to connect. Retry?")

if response:
    print("Retrying")
else:
    print("Cancelled")
    
root.mainloop()