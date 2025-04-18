from selenium_helper.common_code import CommonCode
import os

class New_Tab_link:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.helper.open_url("https://twe.itsfortesza.com/")
        self.driver.switch_to.new_window('window')
        self.helper.open_url("https://demo.nopcommerce.com/")

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    test_script = New_Tab_link()
    test_script.close()
