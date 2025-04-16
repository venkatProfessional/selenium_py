from sys import exception


from selenium.webdriver import ActionChains
from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Drag_drop:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.act = ActionChains(self.driver)

    def drag_drop_automation(self):
        try:
            self.helper.open_url("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette")
            source_ele = self.helper.driver.find_element(By.XPATH,"//div[@id='box3']")
            target_ele = self.helper.driver.find_element(By.XPATH,"//div[@id='box106']")
            self.act.drag_and_drop(source_ele,target_ele).perform()
            self.helper.wait()

        except exception as e:
            print(f"The error occurs {e}")
        finally:
            print("The test case has been finished")

if __name__ == "__main__":
    test = Drag_drop()
    test.drag_drop_automation()




