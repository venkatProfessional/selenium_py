from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
    TimeoutException

from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

browser1 = CommonCode()

browser1.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

myWait = WebDriverWait(browser1.driver,20,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])

email = myWait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']")))
email.send_keys("Admin")

password=myWait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']")))
password.send_keys("admin123")

# this is how senior Automation Tester  write the code
# Create an explicit wait instance
wait = WebDriverWait(browser1.driver, 10)

# Wait until the login button is clickable
try:
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
    login_button.click()
except TimeoutException:
    print("Login button was not found or clickable in time.")

browser1.driver.quit()










