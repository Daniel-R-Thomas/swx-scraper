from selenium import webdriver
from selenium import *
import tkinter as tk
from Tkinter import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.wemainbdriver.common.action_chains import ActionChains
import sys

globalStatus = "Not running..."#will change this later
globalAppName = "Not selected"




def mainGoogleCode():
    try:

        driver = webdriver.Chrome("/home/redrange0/Desktop/sel/drivers/chromedriver")

        driver.set_page_load_timeout(10)
        driver.get("http://www.google.com")

        elem = driver.find_element_by_name("q")
        elem.send_keys("google mail")
        elem.send_keys(Keys.RETURN)

        driver.find_element_by_link_text("Gmail - Google").click()


        time.sleep(2)
        driver.quit()

    except:
        print"something happened :("

fbUsername = "manny.kin.vip@gmail.com"
fbPassword = "N0t4finsta101"
def runFBMain():
    print"Running FaceBook main..."
    mainFBCode()


def mainFBCode():
    #try:
        driver = browser = webdriver.Chrome("/home/redrange0/Desktop/sel/drivers/chromedriver")

        driver.set_page_load_timeout(10)

        FBLogin(driver, 1)



        #screenShot(driver, 'FaceBook')
        time.sleep(5)

        for x in range(0, 5):
            print"Scrolling down the page..."
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            screenShot(driver, 'FaceBook')
            time.sleep(2)



        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)#scroll back to top


        print "Opening FaceBook post..."
        driver.execute_script("var elems = document.getElementsByClassName('img sp_6RczJsWVhIp sx_978b7e');for(var i= 0;i<1;i++){elems[i].click();}")
        time.sleep(2)
        print "Opening like(s)..."
        driver.find_element_by_xpath("//a[contains(@href,'/ufi/reaction/profile/browser/?ft_ent_identifier=')]").click()
        time.sleep(2)
        goBack(driver, -2)









        time.sleep(999999)
        driver.quit()


    #except:
        print"something happened in mainFBCode() :("
        print"Killing itteration until a failsafe can be created"
        driver.quit()


def FBLogin(driver, x):
    try:
        driver.get("http://m.facebook.com")#start login
        time.sleep(2)
        elem = driver.find_element_by_name("email")
        elem.send_keys(fbUsername)
        elem = driver.find_element_by_name("pass")
        elem.send_keys(fbPassword)
        elem = driver.find_element_by_name("login").click()
        time.sleep(2)
        driver.find_element_by_link_text("Not Now").click()



    except:
        print"Login Crashed!"
        driver.quit()
        x = x + 1
        if 5 > x:
            print"Attempting to login again (%d/5)..." % x
            FBLogin(driver,x)

        print"Something's wrong"


def goBack(driver, x):
    print "Backtracking by %d pages..." % x
    stringTest = "window.history.go(%d)" % x
    driver.execute_script(stringTest)



def screenShot(driver, description):
    try:
        print("Saving screenshot from %s to /screenshots" % driver.title)
        currentTime = time.time()
        descriptionString = str(currentTime) + description
        driver.save_screenshot('screenshots/%s.png' % descriptionString)
    except:
        print"Screenshot failed!"





def loopRun():
    for x in range(0, 3):
        mainFBCode()

def infiniteRun():# Change to refresh page and start again from top
    for x in range(0, 10000000):
        mainFBCode()


def runGUI():
    root = tk.Tk()
    root.title("WebScraper - SOFWERX")


    image = tk.PhotoImage(file="images/logo.png")
    label = tk.Label(image=image)
    label.pack()

    l = Label(root, text="Social Media WebScraper\nDaniel R. Thomas")
    l.pack()


    lf = LabelFrame(root, text="Commands:")
    lf.pack()

    t = Label(lf, text="Choose your option:")
    t.grid(columnspan=2, stick='w')

    specialistchoose = IntVar()

    r1 = tk.Button(lf, text="Run Test FaceBook Scrape",fg="blue",command=runFBMain)
    r1.grid(row=1, column=0, stick='w')

    r2 = tk.Button(lf, text="Run Test Google",fg="blue",command=mainGoogleCode)
    r2.grid(row=1, column=1, stick='w')

    r3 = tk.Button(lf, text="Run 3 Itterations",fg="blue",command=loopRun)
    r3.grid(row=1, column=2, stick='w')

    r4 = tk.Button(lf, text="Infinite Run",fg="blue",command=infiniteRun)
    r4.grid(row=2, column=0, stick='w')

    lf1 = LabelFrame(root, text="Data - not working:")
    lf1.pack(side=tk.LEFT)

    t0 = Label(lf1, text="Program: ")
    t0.grid(columnspan=2, stick='w')

    t1 = Label(lf1, text="Status: ")
    t1.grid(columnspan=2, stick='w')

    root.mainloop()

runGUI()
