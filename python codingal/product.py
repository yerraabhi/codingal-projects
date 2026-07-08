from tkinter import *

window=Tk()

window.title("PRODUCT")
window.geometry("400x300")

label1=Label(text="First Number",bg="#FFFFFF")
entry1=Entry()
label1=Label(text="Second Number",bg="#FFFFFF")
entry2=Entry()
label1=Label(text="Product",bg="#FFFFFF")
textbox1=Text(height=1)

num1=entry1.get()
num2=entry2.get()
product=num1*num2

textbox1.insert(product)

window.mainloop()