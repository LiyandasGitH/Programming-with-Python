from hello import hello


def test_default():
    assert hello("Dany") == "hello, Dany"

def test_argument():
   for name in ["Dany", "Jon", "Robb"]:
       assert hello(name) == f"hello, {name}"

'''
def test_hello():
    assert hello("Dany") == "hello, Dany"
    assert hello() == "hello, world"
'''
