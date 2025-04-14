# in this we can see About how to handle links

from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By


browser3 = CommonCode()

browser3.open_url("https://testautomationpractice.blogspot.com/")

# browser3.driver.find_element(By.LINK_TEXT,"Udemy Courses").click()
# partial link
browser3.driver.find_element(By.PARTIAL_LINK_TEXT,"Ude").click()

# total number of links available on the webpage
#  to find the element by TagName

totaLinksTags = browser3.driver.find_elements(By.TAG_NAME,"a")
print(totaLinksTags)

for i in totaLinksTags:
    print(i.text)

# how to handle the broken links


