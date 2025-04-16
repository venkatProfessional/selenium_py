# date picker
# customized non customized
from math import trunc

from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By

browserDriver = CommonCode()
browserDriver.open_url("https://jqueryui.com/datepicker/")

changetheframe = browserDriver.driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
browserDriver.driver.switch_to.frame(changetheframe)

dateinput= browserDriver.driver.find_element(By.ID,"datepicker")

# using sentkeys method
dateinput.send_keys("01/08/2021")
browserDriver.wait()
dateinput.clear()
browserDriver.wait()

# using the datepicker
# store which date you want to select everything in string
year = "2021"
date = "30"
month = "March"

dateinput.click()


while True:
    datepickerMonth = browserDriver.driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    datepickerYear = browserDriver.driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    if year == datepickerYear and month == datepickerMonth:
        break
    else:
        browserDriver.driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        browserDriver.wait()  # optional, gives UI time to update


# select Date

Alldate = browserDriver.driver.find_elements(By.XPATH, "//table//tbody//tr//td//a")
for x in Alldate:
    print(f"Found date: {x.text}")  # Optional: to debug all dates
    if x.text.strip() == date.strip():
        print(f"Clicked date: {x.text}")  # ✅ This prints the clicked date
        x.click()
        break





