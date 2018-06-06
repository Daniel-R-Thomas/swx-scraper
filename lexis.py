from selenium import webdriver
from selenium import *
import time
from selenium.webdriver.common.keys import Keys
#from selenium.wemainbdriver.common.action_chains import ActionChains
import sys
from FBGeneralCode import *


def crimeDataGrabber():
    try:
        driver = browser = webdriver.Chrome("drivers/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://communitycrimemap.com/?address=tampa,fl")

        openEvents(driver)
        selectAllEvents(driver)

        for y in range(0, 20):#opens 20 pages of data
            grabCrimeData(driver, y)
            nextPage(driver)
            time.sleep(3)
        time.sleep(10)

    except:
        print "Crime Data Grabber finished executing."


def grabCrimeData(driver, y):
    try:
        for x in range(0, 20):
            element = driver.find_elements_by_css_selector('div.x-grid3-cell-inner.x-grid3-col-0')[x]#to crash early if null
            print ("\nCrime %d:" % (x+(y*20+1)))
            print "Class: ",
            urlString = element.find_element_by_tag_name('img').get_attribute('src') #this takes the image name
            urlString = urlString.replace('http://communitycrimemap.com/images/icons/key/','')
            urlString = urlString.replace('.png','')
            urlString = urlString.replace('https://communitycrimemap.com/images/icons/key/','')#note https and http difference
            print urlString.title()

            print "Incident: ",
            print driver.find_elements_by_css_selector('div.x-grid3-cell-inner.x-grid3-col-1')[x].text

            print "Crime: ",
            print driver.find_elements_by_css_selector('div.x-grid3-cell-inner.x-grid3-col-2')[x].text

            print "Date/Time: ",
            print driver.find_elements_by_css_selector('div.x-grid3-cell-inner.x-grid3-col-3')[x].text

            print "Address: ",
            address = driver.find_elements_by_css_selector('div.x-grid3-cell-inner.x-grid3-col-5')[x].text
            print address,
            getCords(address)

            print "Accuracy: ",
            print driver.find_elements_by_css_selector('div.x-grid3-cell-inner.x-grid3-col-6')[x].text

            print "Agency: ",
            print driver.find_elements_by_css_selector('div.x-grid3-cell-inner.x-grid3-col-7')[x].text

        time.sleep(2)

    except:
        print"\n"
        driver.quit()


def changeDateRange(driver):#how far back
    driver.find_elements_by_css_selector('div.x-tool.x-tool-toggle')[2].click()
    time.sleep(2)


def openEvents(driver):
        time.sleep(3)
        driver.find_elements_by_class_name(' x-btn-text')[1].click()#if there's any extra pop up
        time.sleep(2)
        driver.find_element_by_class_name(' x-btn-text').click()#second popup
        time.sleep(2)
        driver.find_element_by_link_text("Data Grid").click()
        time.sleep(2)


def selectAllEvents(driver):
    driver.find_elements_by_css_selector('div.x-tool.x-tool-toggle')[3].click()
    time.sleep(2)
    driver.find_element_by_class_name('select-button').click()
    time.sleep(2)
    driver.find_elements_by_css_selector('div.x-tool.x-tool-toggle')[3].click()
    time.sleep(3)


def nextPage(driver):
    driver.find_element_by_css_selector('button.x-btn-text.x-tbar-page-next').click()
