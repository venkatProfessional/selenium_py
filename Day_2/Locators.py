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
# driver.find_element(By.CLASS_NAME,"search-box-text").send_keys("Laptop")
# Wait()
# driver.find_element(By.CLASS_NAME,"search-box-button").click()
# Wait()

#  how to use link and link-text
# driver.find_element(By.LINK_TEXT,"Register").click()
# Wait(20)
# partial link text is used
# driver.find_element(By.LINK_TEXT,"Regi").click()
# Wait()
# RobotXpath = "//*[@id='DPxlC8']/div/label/input"
# driver.find_element(By.XPATH,RobotXpath)

# to find length of the slider

#  use findelements bcoz it have more than one element add s
sliderCount = driver.find_elements(By.CLASS_NAME,"swiper-wrapper")

print(len(sliderCount))

# if sliderlength == 2:
#     print("Slider length case passed")

#  to find how many links available in the webpage

# howManyLinks = driver.find_elements(By.TAG_NAME,'a')
# print(howManyLinks)
# for link in howManyLinks:
#     print(link.get_attribute("href"))  # Get URL of the link
#
# Wait(10)


# lets see how to work with css selectors

# driver.quit()
