from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

# Initialize WebDriver
serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

try:
    driver.get("http://www.deadlinkcity.com/")
    driver.maximize_window()

    allLinks = driver.find_elements(By.TAG_NAME, 'a')
    count = 0

    for link in allLinks:
        url = link.get_attribute('href')  # Extract href attribute

        if url is None or url.strip() == "":
            print("Skipping empty or None URL")
            continue

        try:
            res = requests.head(url, allow_redirects=True, timeout=5)  # Handle redirects, set timeout
            if res.status_code >= 400:
                print(url, "is a broken link")
                count += 1
            else:
                print(url, "is a valid link")

        except requests.exceptions.RequestException as e:
            print(url, "could not be reached due to:", e)
            count += 1  # Consider unreachable links as broken

    print("Total number of broken links:", count)

except Exception as e:
    print("An error occurred while running the script:", e)

finally:
    driver.quit()  # Ensure browser closes properly
