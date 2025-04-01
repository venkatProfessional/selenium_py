
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def delay(seconds =2 ):
    time.sleep(seconds)

serv_obj = Service(r"C:\drivers_selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
delay()
# first parameter is locator
# another one is value
driver.find_element(By.NAME,"username").send_keys("Admin")
delay()

driver.find_element(By.NAME,"password").send_keys("admin123")
delay()

driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
delay(4)

# takes the title of the website
act_title = driver.title
exp_titile = "OrangeHRM"

if act_title == exp_titile:
    print("login passed")
else:
    print("login failed")





driver.quit()

