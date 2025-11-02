from plates import is_valid

def main():
    test_valid1()
    test_valid2()
    test_valid3()
    test_valid4()

def test_valid1():
    assert is_valid("C") == False
    assert is_valid("CS") == True
    assert is_valid("OUTATIME") == False


def test_valid2():
    assert is_valid("CS50") == True
    assert is_valid("CS50B") == False
    assert is_valid("CS05") == False
    assert is_valid("A2") == False


def test_valid3():
    assert is_valid("HELLO!") == False
    assert is_valid("CS50.") == False
    assert is_valid("HELLO1") == True

def test_valid4():
    assert is_valid("CS05") == False
    assert is_valid("CS5") == True






