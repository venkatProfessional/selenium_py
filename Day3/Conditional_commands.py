from faulthandler import is_enabled

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def Wait(seconds =2 ):
    time.sleep(seconds)

service_obj = Service(r"C:\drivers_selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Register.html")
Wait()
driver.maximize_window()
Wait()

# is enabled

Commands = driver.find_element(By.XPATH,"//img[@alt='image not displaying']")

print(Commands.is_enabled())
print(Commands.is_displayed())
print(Commands.is_selected())

checks_isSelected = driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input")
checks_isSelected.click()
print(checks_isSelected.is_selected(),"checks is selected")

Wait()

# driver.close is used to close the parent window when it is opened by link

driver.find_element(By.LINK_TEXT,"Automation Testing")

#  quit command is used to kill the process
#  eg if the 5 browser window opens close is used to close the parent window
#  but the quit is used to kill the kill the full windows'

# navigational commands and navigational methods


