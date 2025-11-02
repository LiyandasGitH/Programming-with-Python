from twttr import shorten

def main():
    test_twttr()

def test_twttr():

   assert shorten("hello") == "hll"
   assert shorten("GOODBYE") == "GDBY"
   assert shorten("hello, world") == "hll, wrld"
   assert shorten("HELLO") == "HLL"




if __name__ == "__main__":
    main()



    '''
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten("23") == "23"
    assert shorten("CS50") == "CS50"
    assert shorten("hello, WORLD") == "hll"
    assert shorten(",._-") == ",._-"
    '''
