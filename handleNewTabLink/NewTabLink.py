from selenium_helper.common_code import CommonCode
import os

class New_Tab_link:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.helper.open_url("https://twe.itsfortesza.com/")

    def automate_screenshot(self, filename="TW.png"):
        screenshot_dir = "E:\\Venkat\\selenium_learning\\handleScreenshot\\screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)  # Ensure directory exists

        filepath = os.path.join(screenshot_dir, filename)
        if self.driver.save_screenshot(filepath):
            print(f"Screenshot saved to: {filepath}")
        else:
            print("Failed to take screenshot.")
        self.helper.wait()

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    test_script = New_Tab_link()
    test_script.automate_screenshot()
    test_script.close()
