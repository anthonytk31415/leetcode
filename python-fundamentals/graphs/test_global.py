# test_global

def test2(z):
    z = z + 1
    

def test1():
    z = 0
    test2(z)
    return z

print(test1())