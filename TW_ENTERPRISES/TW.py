from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime




browser4 = CommonCode()

wait = WebDriverWait(browser4.driver, 10)

browser4.open_url("https://twe.itsfortesza.com/")

browser4.driver.find_element(By.XPATH,"//input[@id='email']").send_keys("admin@gmail.com")
browser4.wait()

browser4.driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Welcome@l1")
browser4.wait()

browser4.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
browser4.wait()

browser4.driver.find_element(By.XPATH,"//div[normalize-space()='Employee Maintenance']").click()
browser4.wait()

browser4.driver.find_element(By.XPATH,"//a[normalize-space()='Create']").click()
browser4.wait()


def convert_date(date_str):
    """Convert DD-MM-YYYY to YYYY-MM-DD"""
    return datetime.strptime(date_str, "%d-%m-%Y").strftime("%Y-%m-%d")

form_fields = [
    # Dropdowns
    {'type': 'dropdown', 'locator': (By.ID, 'expense_type'), 'value': 'TWE'},
    {'type': 'dropdown', 'locator': (By.ID, 'country'), 'value': 'Truewaves Madurai'},
    {'type': 'dropdown', 'locator': (By.XPATH, "(//select[@id='country'])[2]"), 'value': 'MD'},
    {'type': 'dropdown', 'locator': (By.XPATH, "//div[@class='mb-3 col-md-12']//select[@id='country']"), 'value': 'Developer'},
    {'type': 'dropdown', 'locator': (By.XPATH, "(//select[@id='country'])[4]"), 'value': '8AM to 8PM'},

    # Textboxes
    {'type': 'textbox', 'locator': (By.XPATH, "//input[@id='username']"), 'value': 'AjithKumar'},
    {'type': 'textbox', 'locator': (By.XPATH, "//input[@id='email']"), 'value': 'AjithKumar@gmail.com'},
    {'type': 'textbox', 'locator': (By.XPATH, "//input[@id='password']"), 'value': 'Welcome@l1'},
    {'type': 'textbox', 'locator': (By.XPATH, "//input[@id='esi']"), 'value': '121212'},
    {'type': 'textbox', 'locator': (By.XPATH, "//input[@id='empcode']"), 'value': '121212'},
    {'type': 'textbox', 'locator': (By.XPATH, "//input[@id='address']"), 'value': 'test no 121 test'},
    {'type': 'textbox', 'locator': (By.XPATH, "//input[@id='phoneNumber']"), 'value': '9000000005'},

    # Dates
    # {'type': 'date', 'locator': (By.XPATH, "//input[@id='joining_date']"), 'value': '1-12-2024'},
    # {'type': 'date', 'locator': (By.XPATH, "//input[@id='date_of_birth']"), 'value': '10-03-2002'}
]

for field in form_fields:
    locator_type, locator_value = field['locator']
    try:
        element = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))

        if field['type'] == 'dropdown':
            select_obj = Select(element)
            found = False
            for option in select_obj.options:
                if option.text.strip() == field['value']:
                    option.click()
                    found = True
                    print(f"✅ Selected from dropdown '{locator_value}': {field['value']}")
                    break
            if not found:
                print(f"⚠️ Option '{field['value']}' not found in dropdown '{locator_value}'")

        elif field['type'] == 'textbox':
            element.clear()
            element.send_keys(field['value'])
            print(f"✅ Entered in textbox '{locator_value}': {field['value']}")

        elif field['type'] == 'date':
            formatted_date = convert_date(field['value'])
            element.clear()
            element.send_keys(formatted_date)
            print(f"✅ Entered date in '{locator_value}': {formatted_date}")

    except Exception as e:
        print(f"❌ Error handling field '{locator_value}': {str(e)}")

# Wait before submit
browser4.wait(5)

# Submit
try:
    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']")))
    submit_btn.click()
    print("✅ Form submitted.")
except Exception as e:
    print(f"❌ Failed to submit form: {e}")
