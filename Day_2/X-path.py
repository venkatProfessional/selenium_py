from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def Wait(seconds =2 ):
    time.sleep(seconds)

service_obj = Service(r"C:\drivers_selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")
Wait()
driver.maximize_window()
Wait()

driver.find_element(By.XPATH,"//*[@id='email' or @placeholder='Email address or phone number']").send_keys("Abc@gmail.com")
Wait()

# how to click a button by x-path
driver.find_element(By.XPATH,"//button[@type='submit' or @id='loginbutton']").click()
Wait()

# for and both showld be matched
driver.find_element(By.XPATH,"//button[@type='submit' and @id='loginbutton']").click()

# imagine if the button is dynamic how we do a xpath for start and stop
# use contains , startswith and OR

# ways to find
#dont use = because starts with works only by parameter so we use only cama

# //button[@id='loginbutton' or @id='logout']
# //button[contains(@id,'log')]
# //button[starts-with(@id,'log')]

# find by text

# //a[text()='Log in']