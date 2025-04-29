import pytest
# fixture is nothing but pre conditions and post condition
# fixture is also help to load the data

@pytest.mark.usefixtures("setup_fixture")
class TestExample:
    def test_fixuturedemo(self):
        print("it will execute steps in fixture method")
    def test_fixuturedemo1(self):
        print("it will execute steps in fixture method")
    def test_fixuturedemo2(self):
        print("it will execute steps in fixture method")
    def test_fixuturedemo3(self):
        print("it will execute steps in fixture method")
    def test_fixuturedemo4(self):
        print("it will execute steps in fixture method")
    def test_fixuturedemo5(self):
        print("it will execute steps in fixture method")
    def test_fixuturedemo6(self):
        print("it will execute steps in fixture method")
    def test_fixuturedemo7(self):
        print("it will execute steps in fixture method")


# res

# test_fixtureclass.py this is pre condition which runs before the all test cases
# it will execute steps in fixture method
# .it will execute steps in fixture method
# .it will execute steps in fixture method
# .it will execute steps in fixture method
# .it will execute steps in fixture method
# .it will execute steps in fixture method
# .it will execute steps in fixture method
# .it will execute steps in fixture method
# .this is post condition
