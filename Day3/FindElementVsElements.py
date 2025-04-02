from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def Wait(seconds =2 ):
    time.sleep(seconds)

service_obj = Service(r"C:\drivers_selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")
Wait()
driver.maximize_window()
Wait()

# what is the difference between findelement and elements

# locator matching with mutiple web elements
ExampleofElement = driver.find_element(By.XPATH,"//div[@class='footer']//a")
print(ExampleofElement.text) #it returns the first element

ExampleofElements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")

for x in ExampleofElements:
    print(x.text,"Example of elements ")

#     when the no such exceptional returns

driver.find_element(By.LINK_TEXT,"log").send_keys("abc")

#  when the browser able to not find that it returns the no Such exceptional





