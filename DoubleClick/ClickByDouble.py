from selenium.webdriver import ActionChains
from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class DoubleClickTest:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.act = ActionChains(self.driver)

    def run_test(self):
        try:
            # Step 1: Open the test page
            self.helper.open_url("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

            # Step 2: Switch to the iframe containing the input field
            iframe = self.driver.find_element(By.ID, "iframeResult")
            self.driver.switch_to.frame(iframe)

            self.helper.wait()

            # Step 3: Clear the input field and enter text
            input_field = self.driver.find_element(By.ID, "field1")
            input_field.clear()
            input_field.send_keys("Vijay")

            self.helper.wait()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"[ERROR] Setup failed: {e}")
            raise  # So the next step knows this failed

    def doubleClickButton(self):
        try:
            # Double click the button
            double_click_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
            self.act.double_click(double_click_button).perform()

            self.helper.wait()

            # Verify if the text was copied
            result_field = self.driver.find_element(By.ID, "field2")
            copied_text = result_field.get_attribute("value")
            assert copied_text == "Vijay", f"[ASSERTION FAILED] Expected 'Vijay' but got '{copied_text}'"
            print("[INFO] Text copied successfully.")

        except Exception as e:
            print(f"[ERROR] Double-click failed: {e}")

        finally:
            self.driver.quit()
            print("[INFO] Test execution completed and browser closed.")

if __name__ == "__main__":
    test = DoubleClickTest()
    test.run_test()
    test.doubleClickButton()
