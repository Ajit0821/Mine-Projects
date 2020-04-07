import tkinter
from tkinter import *
import random
from tkinter import messagebox
win=tkinter.Tk()
win.geometry("350x400")
win.title("Jumble Words")
win.configure(background="black")
answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]
num=random.randrange(0,6,1)
def default():
    global words,answers,num
    label1.config(text=words[num])

def checkans():
    global words,answers,num
    var=e1.get()
    if(var==answers[num]):
        messagebox.showinfo(message="This answer is Correct")
        res()
    else:
        messagebox.showinfo(message="This is Wrong Answer")
        e1.delete(0,END)
def res():
    global words,answers,num
    num=random.randrange(0,6,1)
    label1.config(text=words[num])
    e1.delete(0,END)

label1=Label(win,text="Hii whats up gyus",font=("Verdana"),bg="black",fg="white")
label1.pack(pady=30)
ans1=StringVar()
e1=Entry(win,font=("Verdana",16),textvariable=ans1)
e1.pack(ipadx=10,ipady=10)
b1=Button(win,text="Check",font=("Comic sans ms",10),width=21,bg="#7B8788",fg="#1BCA9B",relief=GROOVE,command=checkans)
b1.pack(pady=30)

b2=Button(win,text="Reset",font=("Comic sans ms",10),width=21,bg="#7B8788",fg="#3C40C6",relief=GROOVE,command=res)
b2.pack()

default()
win.mainloop()