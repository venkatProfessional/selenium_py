from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for the username field to be present
wait = WebDriverWait(driver, 50)
username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username.send_keys("Admin")

# Find the password field
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

# Find and click the login button
# login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
# login_button.click()

# Close browser
driver.quit()

