from selenium.webdriver import ActionChains
from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By

HoverOBJ = CommonCode()

# Open the website
HoverOBJ.open_url("https://opensource-demo.orangehrmlive.com/")

# Login
HoverOBJ.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
HoverOBJ.wait()
HoverOBJ.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
HoverOBJ.wait()
HoverOBJ.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
HoverOBJ.wait()

# Verify login
title_OrangeHRM = HoverOBJ.driver.title
if title_OrangeHRM == "OrangeHRM":
    print("login successfully test case passed")

# Click on Admin menu
HoverOBJ.driver.find_element(By.CLASS_NAME, "oxd-main-menu-item").click()
HoverOBJ.wait()

# Create ActionChains object
act = ActionChains(HoverOBJ.driver)

# Find User Management element
user_management = HoverOBJ.driver.find_element(By.XPATH, "//span[normalize-space()='User Management']")

# Click on User Management using ActionChains
act.click(user_management).perform()
HoverOBJ.wait()

# Find Users element and click using ActionChains
users = HoverOBJ.driver.find_element(By.XPATH, "//a[normalize-space()='Users']")
act.click(users).perform()

print("Navigation to Users page successful")

# move_to_element is used to howse over actions
# Action chain class options is used for mouse hover
HoverOBJ.driver.close()

HoverOBJ.open_url("https://swisnl.github.io/jQuery-contextMenu/demo.html")


rightclickbutton = HoverOBJ.driver.find_element(By.CLASS_NAME, "context-menu-one")

# How to make a right click scenario in automation
# it is used to right click the element
act.context_click(rightclickbutton).perform()

# handle double click in automation



