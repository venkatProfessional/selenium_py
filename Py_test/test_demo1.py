

def test_firstProgram():
    print("first py test")


def test_checkTwoStrings():
    msg = "Hello"
    assert msg == "Hi","this strings are not same"


def test_additionoftwoInt():
    a = 10
    b = 6
    assert a+b == 10 ,"a + b is not addition of given value"