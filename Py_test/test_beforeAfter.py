import pytest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
# it is like a prerequiste
def test_setup():
    print("this will be executing first")


@pytest.fixture
def test_fixture_demo(setup):
    print("i will execute steps in fixture method")



# example for fixture

# @pytest.fixture
# def driver():
#     # Setup WebDriver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     # Teardown WebDriver
#     driver.quit()
#
#
# def test_valid_login(driver):
#     driver.get("https://example.com/login")
#
#     # Fill in login form
#     driver.find_element(By.ID, "username").send_keys("testuser")
#     driver.find_element(By.ID, "password").send_keys("securepassword")
#     driver.find_element(By.ID, "loginBtn").click()
#
#     # Assert login success (example: checking URL or welcome text)
#     assert "dashboard" in driver.current_url or "Welcome" in driver.page_source@pytest.fixture
# def driver():
#     # Setup WebDriver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     # Teardown WebDriver
#     driver.quit()
#
#
# def test_valid_login(driver):
#     driver.get("https://example.com/login")
#
#     # Fill in login form
#     driver.find_element(By.ID, "username").send_keys("testuser")
#     driver.find_element(By.ID, "password").send_keys("securepassword")
#     driver.find_element(By.ID, "loginBtn").click()
#
#     # Assert login success (example: checking URL or welcome text)
#     assert "dashboard" in driver.current_url or "Welcome" in driver.page_source
