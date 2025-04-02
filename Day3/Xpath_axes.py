# xpath-axes
#xpath axes means top to bottom - bottom to top

# self
# parent
# child
# ancestor
# desecendant
# following
# following-sibling
# preceding
# preceding-sibling

# self is used to capture the value of the text

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def Wait(seconds =2 ):
    time.sleep(seconds)

service_obj = Service(r"C:\drivers_selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")
Wait()
driver.maximize_window()
Wait()


# self is used to capture the text
# self element is nothing but a self node
to_capture = driver.find_element(By.XPATH,"//a[contains(text(),'V-Mart Retail')]/self::a").text
print(to_capture)  #it returns as V-mart detail

ancestor_element = driver.find_element(By.XPATH,"//a[contains(text(),'V-Mart Retail')]/ancestor::tr/child::td[2]").text
print(ancestor_element)

# if we want to print all of the children
# Find all matching elements
ancestor_elements = driver.find_elements(By.XPATH, "//a[contains(text(),'V-Mart Retail')]/ancestor::tr/child::td")
print(len(ancestor_elements),"length of childs")
# Loop through elements and print text
for element in ancestor_elements:
    print(element.text)  # Extract and print text



# example for descendant
descendant = driver.find_elements(By.XPATH,"//a[contains(text(),'V-Mart Retail')]/ancestor::tr/descendant::*")

for c in descendant:
    print(c.text,"descendant texts")


# XPath Axis	What It Does	Direction
# preceding::	Selects all nodes before the current node in the document	Backward ⬆
# following::	Selects all nodes after the current node in the document	Forward ⬇


driver.quit()








