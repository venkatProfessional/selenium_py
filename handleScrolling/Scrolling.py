

from selenium.webdriver import ActionChains
from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class scrolling:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.act = ActionChains(self.driver)
        self.helper.open_url("https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world/")

    def Automate_scrolling(self):
#       scroll down by pixel
#       second parameter will be empty
#       this is a javascript build in function

        self.driver.execute_script("window.scrollBy(0, 3000);")
        y_offset = self.driver.execute_script("return window.pageYOffset;")
        print(y_offset)
        self.helper.wait(5)

#         scroll down the page till the element is visible
        flag = self.driver.find_element(By.XPATH, "//a[normalize-space()='Bulgaria']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.helper.wait(5)

    # Scroll to the very bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.helper.wait(5)


    # Scroll to the very bottom of the page
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        self.helper.wait(5)



if __name__ == "__main__":
    testScript = scrolling()
    testScript.Automate_scrolling()



