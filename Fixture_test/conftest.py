# already conftest file is avialable so it deos not works


import pytest


@pytest.fixture(scope="class")
def setup():
    print("this is pre condition which runs before the all test cases")
    yield
    print("this is post condition ")
