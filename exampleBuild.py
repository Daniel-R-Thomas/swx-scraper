from selenium import webdriver
from selenium import *
import time

driver = webdriver.Chrome("drivers/chromedriver")
driver.set_page_load_timeout(10)



driver.get("http://google.com")
time.sleep(10)
