from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium_helper.common_code import CommonCode
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Select_dropdown:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.helper.open_url("https://twe.itsfortesza.com/")

    def trueWaves(self):
        email = self.helper.driver.find_element(By.XPATH,"//input[@id='email']")
        email.send_keys("Admin@gmail.com")
        password = self.helper.driver.find_element(By.XPATH,"//input[@id='password']")
        password.send_keys("Welcome@l1")
        clickLogin = self.helper.driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
        clickLogin.click()

        self.helper.wait()

        employ_maintanence_ele = self.helper.driver.find_element(By.XPATH,"//div[normalize-space()='Employee Maintenance']")
        employ_maintanence_ele.click()

        create_employ_ele = self.helper.driver.find_element(By.XPATH,"//a[normalize-space()='Create']")
        create_employ_ele.click()

        self.helper.wait()


    def select_select_dropdown(self):
        dropdown_element = self.helper.driver.find_element(By.XPATH,"//select[@id='expense_type']")
        selectoption = Select(dropdown_element)
        alloptions = selectoption.options

        for x in alloptions:
            if x.text == "TWE":
                x.click()
                self.helper.wait()

    def select_role(self):
        role_ele = self.helper.driver.find_element(By.XPATH,"//div[@class='card-body']//div[2]//div[2]//select[1]")
        select_role_options = Select(role_ele).options

        for x in select_role_options:
            if x.text == "Accounts Admin":
                x.click()
                self.helper.wait()

if __name__ == "__main__":
    testScript = Select_dropdown()
    testScript.trueWaves()
    testScript.select_select_dropdown()
    testScript.select_role()



