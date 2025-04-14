from selenium.webdriver.common.by import By
from selenium_helper.common_code import CommonCode
import time

# 100 unique designations with descriptions
designation_data = [

    {"name": "Hardware Technician", "description": "Maintains and repairs physical IT equipment."},
    {"name": "IT Asset Manager", "description": "Tracks company IT assets and hardware."},
    {"name": "Application Developer", "description": "Builds software solutions for business needs."},

]

# Start browser
browser = CommonCode()
browser.open_url("https://twe.itsfortesza.com/")

# Login
browser.driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
browser.wait()
browser.driver.find_element(By.ID, "password").send_keys("Welcome@l1")
browser.wait()
browser.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
browser.wait()



element = browser.driver.find_element(By.XPATH, "//div[normalize-space()='Remainder']")
browser.driver.execute_script("arguments[0].scrollIntoView({block: 'bottom'});", element)
element.click()

