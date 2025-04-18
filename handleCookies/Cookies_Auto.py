from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import time


class CookieHandler:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        time.sleep(2)  # let the page load

    def add_cookie(self, name, value):
        cookie = {
            'name': name,
            'value': value,
            'path': '/',
            # 'domain': 'demo.nopcommerce.com'  # optional
        }
        self.driver.add_cookie(cookie)
        print(f"✅ Cookie added: {name}={value}")

    def update_cookie(self, name, new_value):
        # Delete first, then add with new value
        self.driver.delete_cookie(name)
        self.add_cookie(name, new_value)
        print(f"✏️ Cookie updated: {name}={new_value}")

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)
        print(f"🗑️ Cookie deleted: {name}")

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()
        print("🗑️ All cookies deleted")

    def print_all_cookies(self):
        cookies = self.driver.get_cookies()
        print(f"🔍 Total Cookies: {len(cookies)}")
        for c in cookies:
            print(f"{c['name']} = {c['value']}")

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    cookie_test = CookieHandler()
    # Initial cookies
    cookie_test.print_all_cookies()

    # Add new cookie
    cookie_test.add_cookie("my_test_cookie", "value123")

    # Verify added cookie
    cookie_test.print_all_cookies()

    # Update the cookie
    cookie_test.update_cookie("my_test_cookie", "updated_value456")

    # Verify updated cookie
    cookie_test.print_all_cookies()

    # Delete the cookie
    cookie_test.delete_cookie("my_test_cookie")

    # Delete all cookies (optional)
    # cookie_test.delete_all_cookies()

    # Final cookie state
    cookie_test.print_all_cookies()

    # Close the browser
    cookie_test.close()
