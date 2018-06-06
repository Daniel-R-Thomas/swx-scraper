from selenium import webdriver
from selenium import *
import time
import random
#import json
from selenium.webdriver.common.keys import Keys
#from selenium.wemainbdriver.common.action_chains import ActionChains
import sys
from FBGeneralCode import *
from fileHandler import *


def familyTreeData(firstName, middleName, lastName):
    time.sleep(random.randint(1, 3)) #kinda prevents captchas assuming its not x requests per hour that sets it off


    try:
        driver = browser = webdriver.Chrome("drivers/chromedriver")
        driver.set_page_load_timeout(10)


        #print "Searching for: ",
        #print firstName + " " + middleName + " " + lastName

        #name below works with blank username
        famTreeURL = "https://www.familytreenow.com/search/genealogy/results?first=" + firstName + "&middle=" + middleName + "&last=" + lastName + "&citystatezip=Tampa,%20FL#"
        driver.get(famTreeURL)
        time.sleep(random.randint(2, 7))#more anti captchas
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='summaryResults']/tbody/tr[1]/td/div/div[1]/div[2]/span[2]/a").click()
        time.sleep(1)
        textList = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[2]/div[3]/div/div[9]/table/tbody/tr/td/table/tbody/tr[1]/td")
        time.sleep(1)

        nameString = textList[0].text
        nameString = nameString.replace("\n", "")
        nameString = nameString.replace("Current Address", "")

        time.sleep(random.randint(0, 7))#more anti captchas

        if nameString[0] == "(":#for when the xpath changes and pulls the number section instead
            textList = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[2]/div[3]/div/div[8]/table/tbody/tr/td/table/tbody/tr[1]/td")
            time.sleep(1)

            nameString = textList[0].text
            nameString = nameString.replace("\n", "")
            nameString = nameString.replace("Current Address", "")

        driver.quit()
        return nameString
    except:
        driver.quit()
        return "Unable to find address"


def addressStalk(InputString):
    nameList = InputString.split()#splits name into list from spaces

    if len(nameList) > 3 or len(nameList) < 2:#if  not 2 or 3 then its probably a business name or something weird
        print"Name too short or long to find address"
        return "NULL"

    if len(nameList) == 2:
        altNameString2 = nameList[0] + " " + nameList[1]#probably just use InputString instead
        if checkAddress(altNameString2) == "true":

            print "Address already recorded"
            return "there"

        return familyTreeData(nameList[0], "", nameList[1])

    if len(nameList) == 3:
        altNameString3 = nameList[0] + " " + nameList[1] + " " + nameList[2]
        if checkAddress(altNameString3) == "true":
            print "Address already recorded"
            return "there"

        return familyTreeData(nameList[0], nameList[1], nameList[2])

#addressStalk("Austin Montg Kerr") #testing
