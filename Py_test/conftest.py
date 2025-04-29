# This is a fixture for setup
# fixture will make available on all test cases
import pytest


@pytest.fixture()
def setup():
    print("This will be executed first")

def fixture_demo(setup):
    print("I will execute steps in fixture method")
    yield
    print("This will run last")

@pytest.fixture()
def setup_fixture():
    print("it will be executing first")
    yield
    print("after yield it will be executing last")

#      this is an prefect example
@pytest.fixture(scope="class")
def setup_fixture_test():
    print("this is pre condition which runs before the all test cases")
    yield
    print("this is post condition ")


@pytest.fixture()
def dataLoad():
    print("user profile has been created")
    # returns a tuple
    return ["rahul","shetty","rahulshetty.com"]

@pytest.fixture(params=["chrome","firefix","internetExplorer"])
def crossBrowser(request):
     return request.param


pytest.fixture(params=[
    {"location": "New York", "weight": 5},
    {"location": "Los Angeles", "weight": 10},
    {"location": "Chicago", "weight": 3}
])
def shippingData(request):
    return request.param
