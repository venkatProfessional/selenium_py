from sys import exception

from selenium.webdriver import ActionChains
from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class slider:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.helper.open_url("https://demo.automationtesting.in/Slider.html")
        self.act = ActionChains(self.driver)
    def automate_slider (self):
       try:
           min_ele = self.helper.driver.find_element(By.XPATH,"//a[@class='ui-slider-handle ui-state-default ui-corner-all']")
           # location will return a dictionary
           print(min_ele.location)
           self.helper.wait()
           self.act.drag_and_drop_by_offset(min_ele,"550",0).perform()

       except exception as e :
           print(f"error Occurs {e}")
       finally:
           print("test execution finished")


if __name__ == "__main__":
    testscript = slider()
    testscript.automate_slider()

