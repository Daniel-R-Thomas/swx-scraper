from selenium import webdriver
from selenium import *
import time
import json
from selenium.webdriver.common.keys import Keys
#from selenium.wemainbdriver.common.action_chains import ActionChains
import sys
from FBGeneralCode import *

location = "ybor+tampa"#later can be passed from a gui. + is space

def FBEventScraper():
    try:
        driver = browser = webdriver.Chrome("drivers/chromedriver")
        driver.set_page_load_timeout(10)
        FBLogin(driver)
        fbLocation = ("https://m.facebook.com/graphsearch/str/%s/keywords_events?tsid=0.13098500515814315&source=pivot&ref=content_filter" % location)
        driver.get(fbLocation)
        time.sleep(2)
        populatePage(driver)
        scrollToTop(driver)

        for x in range(0, 21):#will open 21 events. Increase if you want to add more. var could be passed here from GUI
            time.sleep(3)
            grabEventData(driver, x)
            time.sleep(3)

            #goBack(driver, -1)
            driver.get(fbLocation)
            populatePage(driver)#nasty to include this in there but helps reload elements for now. Traversing with new tabs can prevent this

    except:
        print"\nException caught!"
        print"Restarting..."
        driver.quit()
        FBEventScraper()


def grabEventData(driver, x):
    time.sleep(4)
    try:
        print ("Opening Event (%d)..." % x)
        event_list = driver.find_elements_by_class_name('_uok')#opening x event
        event_list[x].click()
        time.sleep(2)
    except:
        print ("Failed to open event (%d)..." % x)
        return





    print "\n\nEvent Name: ",
    eventName = driver.find_element_by_class_name('_31y8').text
    print

    print "Info: ",
    eventInfo = driver.find_element_by_class_name('_31y7').text
    print eventInfo

    print "Date: ",
    eventDate = driver.find_element_by_xpath("//*[@id='event_summary']/div[1]/div[2]/dt/div").text
    print eventDate

    print "Address: ",


    try:#the address IDs names are dynamic and change constantly. A loop running through changing the id name could help a lot
        address = driver.find_elements_by_xpath("//*[contains(@id,'_7')]/div[2]/dd/div")[0].text
    except:
        try:
            address = driver.find_elements_by_xpath("//*[contains(@id,'_6')]/div[2]/dd/div")[0].text
        except:
            try:
                address = driver.find_elements_by_xpath("//*[contains(@id,'_4')]/div[2]/dd/div")[0].text
            except:
                address = driver.find_elements_by_xpath("//*[contains(@id,'_5')]/div[2]/dt/div")[0].text

    print address

    getCords(address)

    time.sleep(1)
    driver.execute_script("return document.body.scrollHeight")
    time.sleep(1)

    '''
    try:
        driver.find_elements_by_class_name('_2058')[1].click()
    except:
        try:
            driver.find_elements_by_class_name('_2058')[2].click()
        except:
            driver.find_elements_by_class_name('_2058')[3].click()
    '''

    for x in range(1,10):#opens names
        try:
            driver.find_elements_by_class_name('_2058')[x].click()#for rare event if there more _2058 elements not names
            break
        except:
            pass

    seeMoreExpand(driver)



    print "Associated names: "
    grabEventNames(driver)
    #goBack(driver, -1)


    time.sleep(2)


def grabEventNames(driver):
    try:
        nameListh3 = []     #<--
        nameListh1 = []
        nameListEvent = []
                            #<--to ensure it's completely empty and nothing leaked over
        del nameListh3[:]
        del nameListh1[:]
        del nameListEvent[:]#<--


        nameListh3 = driver.find_elements_by_css_selector('h3._52jh._5pxc')
        nameListh1 = driver.find_elements_by_css_selector('h1._52jh._5pxc')
        nameListEvent = nameListh1 + nameListh3 #header changes from h3 to h1 for whatever reason
        count = 0

        for x in nameListEvent:
            print ("(%d)" % (count+1)),
            nameString = nameListEvent[count].text
            print nameString,
            #nameAddress = addressStalk(nameString)
            #print nameAddress


            count = count + 1

        time.sleep(2)

        print "\n"
    except:
        print"\nException in grabEventNames\n"
