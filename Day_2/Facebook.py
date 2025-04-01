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

# css selectors tag and id combination   eg tagname#valueofID  input#email
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("ABC@gmail.com")
Wait()

# css selectors tag and class  eg tagname.valueofclass input.password
# "_55r1" is a valid class, but it should be joined with a dot.
# driver.find_element(By.CSS_SELECTOR, "input.inputtext._55r1._6luy._9npi").send_keys("abcsbcbfbvfb")

# tag attribute tagname[attribute="value]
# TAGNAME along with attribute
# Wait()
# driver.find_element(By.CSS_SELECTOR,"input[placeholder='Password']").send_keys("abcsbcbfbvfb")
#
# Wait()

# tag and class attribute
Wait()

driver.find_element(By.CSS_SELECTOR,"input._55r1._6luy._9npi[data-testid=royal-pass]").send_keys("abcsbcbfbvfb")

Wait()
