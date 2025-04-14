from behave import *
from selenium.webdriver.common.by import By
from selenium_helper.common_code import CommonCode

@given(u'i launch the chrome browser')
def step_impl(context):
    context.ob1 = CommonCode()

@when(u'i open orangeHRM home page')
def step_impl(context):
    context.ob1.open_url("https://opensource-demo.orangehrmlive.com/")
    context.ob1.wait()

@when(u'Enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.ob1.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
    context.ob1.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

@when(u'Click login button')
def step_impl(context):
    context.ob1.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    context.ob1.wait()

@then(u'User successfully loged in')
def step_impl(context):
    try:
        text = context.ob1.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert text == "Dashboard", "Dashboard text does not match"
        context.scenario.status = "passed"
    except Exception as e:
        context.scenario.status = "failed"
        assert False, f"Test failed: {str(e)}"
    finally:
        context.ob1.driver.close()