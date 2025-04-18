from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium_helper.common_code import CommonCode
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Select_span_dropdown:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.helper.open_url("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

    def select_span_Example(self):
        visa_application_ele = self.helper.driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']")
        visa_application_ele.click()

        visa_application_options = self.helper.driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']//li")

        for x in visa_application_options:
            if x.text == "India":
                x.click()
                break



        self.helper.wait()




if __name__ == "__main__":
    testScript = Select_span_dropdown()
    testScript.select_span_Example()




