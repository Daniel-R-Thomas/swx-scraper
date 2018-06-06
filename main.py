from selenium import webdriver
from selenium import *
import tkinter as tk
from Tkinter import *
import time
from selenium.webdriver.common.keys import Keys
#from selenium.wemainbdriver.common.action_chains import ActionChains
import sys
from FBCode import *
from FBEventCode import *
from lexis import *
from dispatch import *

def runGUI():
    root = tk.Tk()
    root.title("WebScraper - SOFWERX")


    image = tk.PhotoImage(file="images/logo.png")
    label = tk.Label(image=image)
    label.pack()

    l = Label(root, text="General WebScraper\nDaniel R. Thomas")
    l.pack()


    lf = LabelFrame(root, text="Commands:")
    lf.pack()

    t = Label(lf, text="Choose your option:")
    t.grid(columnspan=2, stick='w')

    specialistchoose = IntVar()

    r1 = tk.Button(lf, text="FaceBook Mainfeed Scrape",fg="blue",command=runFBMain)
    r1.grid(row=1, column=0, stick='w')

    r2 = tk.Button(lf, text="Tampa Bay Dispatch Pull",fg="blue",command=dispatchedCalls)
    r2.grid(row=1, column=1, stick='w')

    r3 = tk.Button(lf, text="FaceBook Event Scrape",fg="blue",command=FBEventScraper)
    r3.grid(row=2, column=0, stick='w')

    r3 = tk.Button(lf, text="Tampa Crime Data Scrape",fg="blue",command=crimeDataGrabber)
    r3.grid(row=2, column=1, stick='w')


    lf1 = LabelFrame(root, text="About:")
    lf1.pack(side=tk.LEFT)

    t0 = Label(lf1, text="The above commands will run with the Selenium WebDriver \nvia Google Chrome.\
 All collected data will eventually be outputted\nin JSONformat to an external file found within the Data folder.")
    t0.grid(columnspan=2)


    root.mainloop()


runGUI()
