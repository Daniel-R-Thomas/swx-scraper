from selenium import webdriver
from selenium import *
import time
from selenium.webdriver.common.keys import Keys
#from selenium.wemainbdriver.common.action_chains import ActionChains
import sys
from FBGeneralCode import *
from tree import *

def runFBMain():#intention was for error handling here
    print"Running FaceBook main..."
    mainFBCode()


def mainFBCode():
    try:
        driver = browser = webdriver.Chrome("drivers/chromedriver")

        driver.set_page_load_timeout(10)

        FBLogin(driver)
        time.sleep(5)

        populatePage(driver)#loads all elements before attempting to grab any

        for x in range(0, 21):#will open 21 elements
            grabData(driver, x)
            populatePage(driver)#nasty to include this in there but helps reload elements for now

        print "Restarting in 6 seconds...\n\n"
        time.sleep(6)
        driver.quit()



    except:
        print"something happened in mainFBCode() :("
        print"restarting..."
        driver.quit()
        runFBMain()


def grabData(driver, x):#opens x event (or specific post)
    scrollToTop(driver)
    print ("Opening FaceBook post (%d)..." % x)

    getLikesElements(driver,x)
    print""
    print"Post Author: ",
    grabPostData(driver)

    time.sleep(2)
    print "Like(s) on post: "
    driver.find_element_by_xpath("//a[contains(@href,'/ufi/reaction/profile/browser/?ft_ent_identifier=')]").click()#specific like event
    time.sleep(2)
    grabNames(driver)
    print"\n"

    time.sleep(2)
    goBack(driver, -2)
    time.sleep(2)


def getLikesElements(driver,x):#opens the specific x event

    try:
        time.sleep(3)
        event_list = driver.find_elements_by_class_name('_1g06')
        event_list[x].click()

    except:
        print"Unable to open more posts..."
        print"Restarting...\n\n"
        runFBMain()
