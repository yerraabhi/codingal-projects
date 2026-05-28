# from tkinter import *

# root=Tk()
# root.title("Number Pad")
# root.geometry("250x300")

# nums=[[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]

# for i in range (4):
#     root.columnconfigure(i,weight=1,minsize=75)
#     root.rowconfigure(i,weight=1,minsize=50)
#     for j in range(0,3):
#         frame=Frame(
#             master=root,
#             relief=SUNKEN,
#             borderwidth=1
#         )
#         frame.grid(row=i,column=j)
#         label=Label(master=frame,text=nums[i][j],bg="#d0efff")
#         label.pack(padx=3,pady=3)

# root.mainloop()

from tkinter import *

root=Tk()
root.title("Login App")
root.geometry("400x400")

frame=Frame(master=root,height=200,width=360,bg="#d0efff")

lbl1=Label(frame,text="Full Name",bg="#3895D3",fg="white",width=12)
lbl2=Label(frame,text="Email Id",bg="#3895D3",fg="white",width=12)
lbl3=Label(frame,text="Enter Password",bg="#3895D3",fg="white",width=12)

nameentry=Entry(frame)
emailentry=Entry(frame)
passentry=Entry(frame,show="*")

def display():
    name=nameentry.get()
    greet="Hey "+name
    message="\nCongratulations for your new account"
    textbox.insert(END,greet)
    textbox.insert(END,message)

textbox=Text(bg="#BEBEBE",fg="black")

btn=Button(text="Create Account",command=display,bg="red")

frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
nameentry.place(x=150,y=20)
lbl2.place(x=20,y=80)
emailentry.place(x=150,y=80)
lbl3.place(x=20,y=140)
passentry.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)

root.mainloop()