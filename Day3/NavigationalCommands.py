from faulthandler import is_enabled

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def Wait(seconds =2 ):
    time.sleep(seconds)

service_obj = Service(r"C:\drivers_selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://demo.automationtesting.in/Register.html")
driver.get("https://snapdeal.com/")
Wait()
driver.maximize_window()
Wait()
#  open two pages in the one tab and go back to the same page
driver.get("https://www.facebook.com/")
Wait()

driver.back()
Wait()
driver.forward()
Wait()
driver.refresh() # refresh is used to refresh the page
Wait()

