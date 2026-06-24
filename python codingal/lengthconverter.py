from tkinter import *

window=Tk()
window.title("Length Conerter App")
window.geometry("400x400")

inches=int(input("Enter length in inches:"))

centimeters=inches*2.54

print(inches,"inches=",centimeters,"cenntimeters.")