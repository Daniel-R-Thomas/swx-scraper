from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def dispatchedCalls():
    driver = browser = webdriver.Chrome("drivers/chromedriver")
    driver.set_page_load_timeout(10)
    driver.get("https://apps.tampagov.net/CallsForService_Webapp/Default.aspx?type=TPD")


    driver.find_element_by_id('ctl00_MainContent_RadGrid1_ctl00_ctl02_ctl00_PageSizeComboBox_Arrow').click()
    time.sleep(.3)
    driver.find_element_by_xpath("//*[@id='ctl00_MainContent_RadGrid1_ctl00_ctl02_ctl00_PageSizeComboBox_DropDown']/div/ul/li[3]").click()
    time.sleep(.5)

    for y in range(0, 50):
        pullDataFromSinglePageLoop(driver)
        driver.find_element_by_xpath("//*[@id='ctl00_MainContent_RadGrid1_ctl00']/thead/tr[1]/td/div/div[4]/button[1]").click()


    time.sleep(5)
    driver.quit()

def pullDataFromSinglePageLoop(driver):
    for x in range(0, 50):
        try:
            print x
            dateString = "//*[@id='ctl00_MainContent_RadGrid1_ctl00__" + str(x) + "']/td[1]"
            addressString = "//*[@id='ctl00_MainContent_RadGrid1_ctl00__" + str(x) + "']/td[2]/a"
            descriptionString = "//*[@id='ctl00_MainContent_RadGrid1_ctl00__" + str(x) + "']/td[3]"
            gridString = "//*[@id='ctl00_MainContent_RadGrid1_ctl00__" + str(x) + "']/td[4]/a"
            reportString = "//*[@id='ctl00_MainContent_RadGrid1_ctl00__" + str(x) + "']/td[5]"

            print "Date: " + driver.find_element_by_xpath(dateString).text
            print "Address: " + driver.find_element_by_xpath(addressString).text
            print "Description: " + driver.find_element_by_xpath(descriptionString).text
            print "Grid: " + driver.find_element_by_xpath(gridString).text
            print "Report: " + driver.find_element_by_xpath(reportString).text + "\n"
        except:
            pass
