from numb3rs import validate


def main():
    test_ip_true()
    test_ip_false()




def test_ip_true():
    assert validate("127.0.0.1") == True
    assert validate("12.13.3.123") == True




def test_ip_false():
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.555.555.555") == False






if __name__ == "__main__":
    main()
