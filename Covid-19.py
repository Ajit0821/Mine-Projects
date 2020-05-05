import requests
import bs4
import plyer
import tkinter
import time
import datetime
import threading


def get_html_data(url):
    data = requests.get(url)
    return data


url='https://www.mohfw.gov.in/'
html_data=get_html_data(url)
bs=bs4.BeautifulSoup(html_data.text, 'html.parser')
info_div = bs.find('div',class_='site-stats-count').find('ul')
active_status=info_div.find('li',class_='bg-blue').find('strong')
cured = info_div.find('li', class_='bg-green').find('strong')
death = info_div.find('li', class_='bg-red').find('strong')
a="Active Cases:- "+str(active_status.get_text())
c="Cured:- "+str(cured.get_text())
d="Death:- "+str(death.get_text())

def refresh():
    Label1['text']="Active Cases:- "+str(active_status.get_text())
    Label2['text'] = "Cured:- "+str(cured.get_text())
    Label3['text'] ="Death:- "+str(death.get_text())
    print("refreshing")




win=tkinter.Tk()
win.title("Corona Live Tracker")
win.geometry("500x500")
win.config(bg="#576574")
f = ('poppins',25,"bold")
Label1 = tkinter.Label(win, text=a, font=f,bg="#8395a7")
Label1.pack()
Label2 = tkinter.Label(win, text=c, font=f,bg="#8395a7")
Label2.pack(pady=15)
Label3 = tkinter.Label(win, text=d, font=f,bg="#8395a7")
Label3.pack(pady=15)

button1=tkinter.Button(text="Refresh",font=('popins',15,"bold"),relief='solid', command=refresh)
button1.pack(ipadx=20,ipady=6,pady=15)

def notify():
    while True:
        plyer.notification.notify(
            title="Covid-19 Notification",
            message = "Active Cases:- "+str(active_status.get_text()),
            timeout=5
            )
        time.sleep(30)

th = threading.Thread(target=notify)
th.setDaemon(True)
th.start()
win.mainloop()