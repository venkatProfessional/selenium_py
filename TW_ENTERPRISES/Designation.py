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

# Go to Designation tab
browser.driver.find_element(By.XPATH, "//div[normalize-space()='Designation']").click()
browser.wait()

# Loop through 100 entries
for entry in designation_data:
    browser.driver.find_element(By.XPATH, "//a[normalize-space()='Create']").click()
    browser.wait()

    browser.driver.find_element(By.ID, "name").send_keys(entry["name"])
    browser.wait()

    browser.driver.find_element(By.ID, "description").send_keys(entry["description"])
    browser.wait()

    browser.driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
    browser.wait()

    time.sleep(1)  # Optional: add wait for any success message

browser.driver.quit()
