from faulthandler import is_enabled

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def Wait(seconds =2 ):
    time.sleep(seconds)

service_obj = Service(r"C:\drivers_selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
Wait()
driver.maximize_window()
Wait()

print(driver.title)
print(driver.current_url) # current url is used to take the current url of the page
print(driver.page_source) # is used to to take the source content of the page


#  conditional Commands
# is_displayed()
# is_enabled()
# is_selected()

