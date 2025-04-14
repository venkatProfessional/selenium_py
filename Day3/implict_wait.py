from selenium_helper.common_code import CommonCode
from selenium import webdriver
from selenium.webdriver.common.by import By


# Create an instance of CommonCode (no need to pass the path)
browser = CommonCode()

# Open Snapdeal
browser.open_url("https://www.google.com/")
googleSearch =browser.driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
browser.driver.implicitly_wait(5)

googleSearch.send_keys("Selenium")
browser.wait()
googleSearch.submit()
browser.wait(10)


browser.driver.quit()
# //*[@id="recaptcha-anchor"]/div[1]
# browser.driver.find_element(By.XPATH,"//*[@id='recaptcha-anchor']/div[1]").click()

# in browser.wait it will create a function inside the class
# so it was time.sleep
# instaed of time.sleep we need to follow the implit wait
# bcoz eg if use time sleep by 5 by 10 times it take 50 seconds time delay performance of the script will become slow
#  so we need to use implict wait
# time is provided by python
# implict wait is provided b selenium web driver







