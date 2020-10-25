# plyer  for windows pop up notification menu

## Importing all the required libraries

import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
from tkinter import Tk, Label
from PIL import Image, ImageTk
import  threading

## getting html data of the website..

def get_data(url):
    data = requests.get(url)
    return data


## parsing html and extracting the data..
def corona_india_data():
    url = 'https://www.worldometers.info/coronavirus/country/india/'
    html_data = get_data(url)
    print(html_data.text) ## getting text from the html
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    # print(bs.prettify())
    info = bs.find("div",class_="content-inner").find_all("div",id="maincounter-wrap")
    #print(len(info))
    #print(info)
    all_details = ""

    for item in info:
        count = item.find('span').get_text() #--> getting values within a span
        text = item.find('h1').get_text() # ---> getting values within header
        #print(text + " : " + count)
        all_details = all_details + text + "  " + count + "\n"
    #print(all_details)

    return all_details

        #print(item.find("span",class_="maincounter-number").get_text())
        #try:
           # count = block.find("span", class_="maincounter-number").get_text()
        #except AttributeError:
           # print('Error')'''
        #count = block.find("span", class_='maincounter-number').get_text()
        #text = block.find("div",id='maincounter-wrap').get_text()
        #print(text + ':' + count)
        #print(count)

## Writing a function to reload the data from website

def refresh():

    new_data = corona_india_data()
    print("Refreshing...")
    mainLable['text'] = new_data #--> setting data to mainlable


'''Function for notifying'''
def notify():
    while True:
        plyer.notification.notify(
            title="Covid 19 cases of India",
            message=corona_india_data(),
            timeout=10,
            app_icon='covid.ico'
        )
## now we will fire our notification after some time
        time.sleep(30) ##--> will get notification after this much time




## Creating GUI::

root = tk.Tk()  ##Tk will create a pop up window for us
root.geometry("500x500")       ##--> set height and width
root.iconbitmap("covid.ico")   ## setting icon
root.title("Corona Data Tracker India")
root.configure(background='#33CCCC')
f = ("poppins",25,"bold") #---> setting font

## setting banner for our popup

#banner = tk.PhotoImage(Image.open("logo.png").resize(10, 10))

banner = tk.PhotoImage(file="covid_tra.png")
bannerLable = tk.Label(root,image=banner)
bannerLable.pack()


mainLable = tk.Label(root,text = corona_india_data(),font=f,bg='#33CCCC')
mainLable.pack()

# creating a refresh button

rebutton = tk.Button(root,text="Refresh",font=f,relief='solid',command=refresh,bg='#808080')
# command is used to get data from refresh function..so we can get new data..don't recall function..just give name
rebutton.pack()


# Create a new thread
th1 = threading.Thread(target=notify)
th1.setDaemon(True) #-->making service provider thread..so when we close app notification will be off..
# making it true will kill the process and you wont get any notification.
th1.start()
root.mainloop()
