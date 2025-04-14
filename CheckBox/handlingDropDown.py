from selenium.webdriver.support.select import Select


from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By


browser3 = CommonCode()

browser3.open_url("https://practice.expandtesting.com/dropdown")

# what id tag name of dropdown
# select is the tag name of dropdown

drpcountry_ele = browser3.driver.find_element(By.XPATH,"//select[@id='country']")

# there was a predefine class called select
# Select is a class we have to create an object
selectObj = Select(drpcountry_ele)

# select option for the dropdown
# most used option is select_by_visible_text
#
# browser3.wait()
# selectObj.select_by_visible_text("India")
# browser3.wait()
#  it will return the total number of options
alloptions = selectObj.options
print(len(alloptions),"total length of the options")
# 252 total length of the options



# print total number of options
# in this all the options has been printed
for x in alloptions:
    print(x.text)

# interview question
#  without using build in function how the how you will find the option?
# this is the way we use without the build in function


AllCountries = selectObj.options

for x in AllCountries:
    if(x.text == "India"):
        x.click()
        break




