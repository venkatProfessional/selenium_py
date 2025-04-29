import pytest


def return_example():
    return 1
    return 2

def yield_example():
    yield 1
    yield 5


print(return_example())

gen = yield_example()


# next() is a built-in function in Python.
# # It is used to manually get the next value from an iterator or generator.
# # Each time you call next(), Python executes the code up to the next yield in a generator function.

print(next(gen),"example of yield and next")
print(next(gen),"example of yield and next")


# yield with fixture demo

# there was a fixture in conftest.py file
# fixture will make available on all test cases


def test_fixture_demo(setup_fixture):
    print("this is the fixture demo")


print(test_fixture_demo)

# Real - Time Example:
# import pytest
# from selenium import webdriver
#
#
# # we can also insert a file in conftest.py to coomonly defined and used in all files
# @pytest.fixture()
# def setup():
#     print("Launching the browser...")
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     print("Closing the browser...")
#     driver.quit()
#
# def test_open_google(setup):
#     print("Navigating to Google...")
#     setup.get("https://www.google.com")
#     assert "Google" in setup.title
