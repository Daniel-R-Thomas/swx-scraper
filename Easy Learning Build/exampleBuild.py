from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def main():
    try:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome("drivers/chromedriver", chrome_options=options)#location of driver

        driver.set_page_load_timeout(10)#how long to wait before ending program
        driver.get("http://www.baynews9.com/fl/tampa/weather")


        CurrentTemp = driver.find_element_by_class_name('current-tempf').text
        print "Current temperature in Tampa: " + CurrentTemp

        chanceRain = driver.find_element_by_class_name('precip-num').text
        print "Current of rain in Tampa: " + chanceRain

        driver.quit()#exit chrome web driver

    except:
        pass
for x in range(0, 50):

    main()
