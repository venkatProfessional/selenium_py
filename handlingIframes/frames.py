from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By

browserDriver = CommonCode()
browserDriver.open_url("https://demo.automationtesting.in/Frames.html")

# Switch to the iframe using a located WebElement
iframe_element = browserDriver.driver.find_element(By.XPATH, "//iframe[@id='singleframe']")
browserDriver.driver.switch_to.frame(iframe_element)

# Now interact with the input box inside the iframe
browserDriver.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("hi")

# Optional: Switch back to the main page if needed
# default content is ued to switch to the main page
browserDriver.driver.switch_to.default_content()
browserDriver.wait()
browserDriver.driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
browserDriver.wait()


outerIframe= browserDriver.driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
browserDriver.driver.switch_to.frame(outerIframe)

innerFrame = browserDriver.driver.find_element(By.XPATH,"//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
browserDriver.driver.switch_to.frame(innerFrame)

browserDriver.driver.find_element(By.XPATH,"//input[@type='text']").send_keys("AbC")

browserDriver.driver.switch_to.default_content()

browserDriver.wait()

browserDriver.driver.find_element(By.XPATH,"//a[normalize-space()='Single Iframe']").click()

browserDriver.wait()
