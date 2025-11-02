from bank import value


def main():
    test_value1()
    test_value2()
    test_value3()



def test_value1():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("  hello   ") == 0

def test_value2():
    assert value("h") == 20
    assert value("hi") == 20
    assert value("  hey ") == 20

def test_value3():
    assert value("What's up") == 100
    assert value("yo") == 100
    assert value("  what up doe ") == 100


if __name__ == "__main__":
    main()
