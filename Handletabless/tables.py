# Example Code
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/table-sort-search-demo.html")
driver.maximize_window()

time.sleep(2)

while True:
    # Locate all rows in the table body
    rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")

    for row in rows:
        # Skip rows with 'No matching records found'
        if 'No matching records' in row.text:
            continue
        # Extract Name and Position from each row
        name = row.find_element(By.XPATH, "./td[1]").text
        position = row.find_element(By.XPATH, "./td[2]").text
        print(f"Name: {name} | Position: {position}")

    # Try to go to the next page
    next_button = driver.find_element(By.ID, "example_next")
    class_attr = next_button.get_attribute("class")

    if "disabled" in class_attr:
        break  # No more pages
    else:
        next_button.click()
        time.sleep(2)

driver.quit()
