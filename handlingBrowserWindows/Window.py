# browser windows
# switchto.window(WindowID)
from day_one.Login import driver
from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By


browserwindow = CommonCode()

browserwindow.open_url("https://opensource-demo.orangehrmlive.com/")

#  how to get an windowID

currentWindowID = browserwindow.driver.current_window_handle
print(currentWindowID)

browserwindow.driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

# to get the browser id or both the windows
windowIDs = browserwindow.driver.window_handles

parentWindowIDOne = windowIDs[0]
parentWindowIDtwo = windowIDs[1]

# my my cursor foucs to send browser
browserwindow.driver.switch_to.window(parentWindowIDtwo)
childtitle = browserwindow.driver.title
print(childtitle)

browserwindow.driver.switch_to.window(parentWindowIDOne)

Parenttitle  = browserwindow.driver.title
print(Parenttitle)


# to get the both windows id
for x in windowIDs:
    print(x)

#
# for winid in windowIDs:
#     driver.switch_to.window(winid)
#     if driver.title == "OrangeHRM HR Software | Free HR Software | HRMS | HRIS":
#         driver.close()

browserwindow.driver.close()