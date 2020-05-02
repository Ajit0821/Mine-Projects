import requests
import tkinter
from tkinter import *
def info():
    Label2=Label(win,text='')
    city=entry.get()
    api_address="http://api.openweathermap.org/data/2.5/weather?appid=3defd2c9a687fd9ebf60c5534fd71a33&q="
    url=api_address+city
    json_data=requests.get(url).json()
    formatted_data=json_data['weather'][0]['description']
    v.set(formatted_data)
    data=int(json_data['main']['temp'])-273
    k.set(str(data)+" Celcius")
    

win=tkinter.Tk()
win.geometry('500x500')
Label1=Label(win,text="Enter the city",font=('verdana',15))
Label1.pack(pady=30)
entry=Entry(win,font=('verdana',25))
entry.pack(ipadx=10,ipady=10)
b1=Button(win,text='Click',width=20,command=info)
b1.pack(padx=15,ipady=15,pady=30)
v = StringVar()
Label2=Label(win,font=('verdana',15), textvariable=v).pack()
k=StringVar()
Label3=Label(win,font=('verdana',15), textvariable=k).pack()
win.mainloop()
