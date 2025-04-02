from selenium_helper.common_code import CommonCode
from selenium import webdriver
from selenium.webdriver.common.by import By


# Create an instance of CommonCode (no need to pass the path)
browser = CommonCode()

# Open Snapdeal
browser.open_url("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

loginemail = browser.driver.find_element(By.XPATH,"//input[@id='Email']")
browser.wait()
loginemail.clear()
browser.wait()
loginemail.send_keys("Abc@gmail.com")

# text returns the inner text in the HTML where it is visible in inspect
# text always returns a inner text
#  get attribute is a functions it returns values in the text box

print(loginemail.text)
print(loginemail.get_attribute('value'))
