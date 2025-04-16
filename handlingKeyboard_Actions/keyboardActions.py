# ctrl+A
# crtl+c
# ctrl+v

# how to do in keyboard Actions

from selenium.webdriver import ActionChains, Keys
from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class keyboard_actions:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.helper.open_url("http://textcompare.com/")
        self.act = ActionChains(self.driver)

    def Automate_keyboard(self):
        TextAreaOne = self.driver.find_element(By.XPATH,"//textarea[@name='frm_compare_1']")
        TextAreaTwo = self.driver.find_element(By.XPATH,"//textarea[@name='frm_compare_2']")

        TextAreaOne.send_keys("welcome to Selenium")
        self.helper.wait(4)
        self.act.key_down(Keys.CONTROL)
        self.act.key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).perform()

#        by pressing the tab key
        self.helper.wait()
        self.act.send_keys(Keys.TAB)  # Press TAB to focus next field
        self.act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        self.helper.wait()

if __name__ == "__main__":
    testScript = keyboard_actions()
    testScript.Automate_keyboard()



