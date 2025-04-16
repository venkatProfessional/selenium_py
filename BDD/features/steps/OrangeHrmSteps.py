from behave import given,when,then


from selenium_helper.common_code import CommonCode
from selenium.webdriver.common.by import By



@given(u'launch chorme browser')
def launch_Browser(context):
    context.browser6 = CommonCode()
    context.browser6.service_obj()

@when(u'open orange HRM home page')
def openHomePage (context):
    context.browser6.open_url("https://opensource-demo.orangehrmlive.com/")


@then(u'verify the logo presence or not')
def verifyLogo(context):
    status = context.browser6.driver.find_element(By.XPATH,"//img[@alt='company-branding']").is_displayed()
    assert  status is True


@then(u'close Browser')
def closeBrowser(context):
    context.browser6.driver.close()

