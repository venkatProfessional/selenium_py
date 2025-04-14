from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By


browser4 = CommonCode()

browser4.open_url("https://the-internet.herokuapp.com/javascript_alerts")

browser4.driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
browser4.wait()

alertWindow = browser4.driver._switch_to.alert

# it will takes the text of the alert box
print(alertWindow.text)

# did not see the values which is entering or not
alertWindow.send_keys("Welcome")
browser4.wait()

# to click the Ok in the alert box
# alertWindow.accept()
# browser4.wait()

# to click cancel in the alert box
alertWindow.dismiss()
browser4.wait()




