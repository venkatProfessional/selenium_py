from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By

browser2 = CommonCode()

browser2.open_url("https://testautomationpractice.blogspot.com/")

# browser2.driver.find_element(By.XPATH,"//input[@id='sunday']").click()

#  it cliks all the dates
daysclick = browser2.driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')] ")

# approach one
# for x in daysclick:
#     x.click()

# Approach Two

# for x in range(len(daysclick)):
#     daysclick[x].click()

 # select mutiple checkbox by choice

# for x in daysclick:
#     getchoice = x.get_attribute('id')
#     if getchoice == "monday" or getchoice == "tuesday":
#         x.click()
#
# browser2.wait(4)

# how to take a last numbers in the checkbox

for x in range(len(daysclick)-2,len(daysclick)): #range 5 to 7
    daysclick[x].click()

#     clearing all the selected checkbox

browser2.wait()

for i in daysclick:
    if i.is_selected():  # Check if the checkbox is selected
        i.click()  # Click to uncheck it


