from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

window=Tk()
window.title("Codingals Text Editor")
window.geometry("600x500")
window.rowconfigure(0,minisize=800,weight=1)
window.columnconfigure(1,minisize=800,weight=1)

def openfile():
    """Open a file for editing"""
    filepath=askopenfilename(
        filetypes=[("Text Files","*.txt"),("All files","*.*")]
    )

    if not filepath:
        return
    
    txt_edit.delete(1.0,END)

    with open(filepath,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    window.title(f"Codingals Text Editor - {filepath}")

def savefile():
    filepath=asksaveasfilename(
        defaultextension="txt"
        filetypes=[("Text Files","*.txt"),("All files","*.*")]
    )

    if not filepath:
        return
        
    with open(filepath,"w") as output_file:
        txt_edit.get(1.0,END)
        output_file.write(text)
    window.title(f"Codingals Text Editor - {filepath}")

txt_edit=Text(window)
fr_buttons=Frame(window,relief=RAISED,bd=2)
btn_open=Button(fr_buttons,"Open",command=openfile)
btn_save=Button(fr_buttons,"Save As...",command=savefile)

btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)
fr_buttons.grid(row=1,column=0,sticky="ns")
txt_edit.grid(row=1,column=0,sticky="nsew")

window.mainloop()