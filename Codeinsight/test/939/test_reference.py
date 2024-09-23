from functools import reduce
def test(str0, str1):
    return reduce(lambda x, y: x + str0 + y, str1)
