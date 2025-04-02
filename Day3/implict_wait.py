from selenium_helper.common_code import CommonCode
from selenium import webdriver
from selenium.webdriver.common.by import By


# Create an instance of CommonCode (no need to pass the path)
browser = CommonCode()

# Open Snapdeal
browser.open_url("https://www.google.com/")
googleSearch =browser.driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
browser.wait()

googleSearch.send_keys("Selenium")
browser.wait()
googleSearch.submit()
browser.wait(50)

browser.driver.quit()
# //*[@id="recaptcha-anchor"]/div[1]
# browser.driver.find_element(By.XPATH,"//*[@id='recaptcha-anchor']/div[1]").click()
