from selenium import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.keys import Keys
#from selenium.wemainbdriver.common.action_chains import ActionChains
import sys
import re
from geopy.geocoders import Nominatim
from tree import *
from fileHandler import *


def accountFetech(infoType):
    accountFile = open("/home/redrange0/Desktop/account(DontUpload)/account.txt","r")#change to your own directory

    #or have it directly return the password below
    #this is made so the password wont get accidentally uploaded

    count = 0
    for line in accountFile:
        if infoType == "user":
            fbUsername = line.replace("\n", "")
            return fbUsername
        elif infoType == "pass" and count == 0:
            count = count + 1
        elif infoType == "pass" and count == 1:
            fbPassword = line.replace("\n", "")
            return fbPassword



def populatePage(driver):
#file will check if the end of the page is met by checking the height of the page
#has any changes after attempting to scroll
        print"Scrolling down the page. This may take some time..."
        height = 0
        endOfFileCheck = 0

        for x in range(0, 150):# any page longer than 150 itterations is too long
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            checkHeight = driver.execute_script("return document.body.scrollHeight")
            if height != checkHeight:
                endOfFileCheck = 0
            if height == checkHeight and endOfFileCheck != 3:
                endOfFileCheck = endOfFileCheck + 1
                time.sleep(1)
            if height == checkHeight and endOfFileCheck == 3:
                print "End of page... breaking"
                break
            height = driver.execute_script("return document.body.scrollHeight")
            time.sleep(.8)

        time.sleep(.5)


def scrollToTop(driver):
    print"Scrolling to top of page..."
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)#scroll back to top
    time.sleep(.2)


def goBack(driver, x):#x = how many pages to scrool back
    print "Backtracking by %d pages..." % x
    stringTest = "window.history.go(%d)" % x
    driver.execute_script(stringTest)


def screenShot(driver, description):#not working, currenty printing blackboxes need to send different driver file
    try:
        print("Saving screenshot from %s to /screenshots" % driver.title)
        currentTime = time.time()
        descriptionString = str(currentTime) + description
        driver.save_screenshot('screenshots/%s.png' % descriptionString)
    except:
        print"Screenshot failed!"


def FBLogin(driver):
    try:
        driver.get("http://m.facebook.com")#start login
        time.sleep(2)
        elem = driver.find_element_by_name("email")
        elem.send_keys(accountFetech("user"))

        elem = driver.find_element_by_name("pass")

        elem.send_keys(accountFetech("pass"))
        elem = driver.find_element_by_name("login").click()
        time.sleep(2)
        driver.find_element_by_link_text("Not Now").click()

    except:
        print"Double login failed. Entering single login state..."
        time.sleep(1)
        elem = driver.find_element_by_name("email")
        elem.send_keys(u'\ue007')
        time.sleep(2)
        elem = driver.find_element_by_name("pass")
        elem.send_keys(accountFetech("pass"))
        elem = driver.find_element_by_name("login").click()
        time.sleep(2)
        driver.find_element_by_link_text("Not Now").click()


def grabNames(driver):
    #name_list = driver.find_element_by_xpath("//*[starts-with(@id='u_)'']/div[1]/header/div[2]/div/div/div[1]/h3/strong/a")
    name_list = driver.find_elements_by_tag_name("strong")#names in the post are only in strong tag

    if len(name_list) > 50:#checks if seeMoreExpand needs to be ran to avoid delay
        seeMoreExpand(driver)

    name_list = driver.find_elements_by_tag_name("strong")#repopulates the additonally loaded names

    count = 0
    for x in name_list:
        nameString = x.text
        if bool(re.search('[a-zA-Z]', nameString)) == True:#skips over blank elents ie. not names
            count = count + 1
            print "(%d)" % count,
            print nameString + ":"
            nameAddress = addressStalk(nameString)
            if str(nameAddress) == "there" or str(nameAddress) == "NULL":#addressStalk returns there if already recorded. NULL if cant find
                pass
            else:
                print nameAddress
                appendToAddress(nameString, nameAddress)

        if count == 10:#comment this out if you want it to record more than the 10 names per post
            break


    print ""


def grabPostData(driver):
    time.sleep(2)

    #name_list = driver.find_elements_by_tag_name("strong")
    name_list = driver.find_elements_by_css_selector("a[href*='__tn__=C-R']")

    postAuthor = ""

    try:
        postAuthor = name_list[0].text
        print postAuthor
    except:
        try:
            name_list = driver.find_elements_by_class_name('actor')#grabs the blue names too now
            postAuthor = name_list[0].text
            print postAuthor
        except:
            print "Null"

    authorAddress = addressStalk(postAuthor)

    if str(authorAddress) == "there" or str(authorAddress) == "NULL":
        pass
    else:
        print authorAddress
        appendToAddress(nameString, authorAddress)


    print "Unique Post ID: ",
    urlString = driver.current_url.replace('https://m.facebook.com/','')
    print urlString

    print "Type: ",
    print urlString.split('.')[0]#posts the single name here


def seeMoreExpand(driver):
#this could be written with less lines of code or maybe more efficently
#but this works fine and doesn't bog anything down hence why it's not changed
    count = 0
    for x in range(0, 50): #spam click first

        try:
            time.sleep(.2)
            driver.find_element_by_partial_link_text("See More").click()
        except:
            count = count + 1
            if count == 20:
                break


    count = 0
    for x in range(0, 50): #slower run through
        try:
            time.sleep(.6)
            driver.find_element_by_partial_link_text("See More").click()
        except:
            count = count + 1
            if count == 3:
                break


def getCords(address):#finds cords of given address
#this uses the from geopy.geocoders import Nominatim
#works okay but not as good as Googles. Googles costs money though, this is free
    try:
        geolocator = Nominatim()
        location = geolocator.geocode(address)
        print((location.latitude, location.longitude))

    except:
        print "[Address Location Error]"
