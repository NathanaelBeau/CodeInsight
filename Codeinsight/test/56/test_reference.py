from functools import reduce

def test(lst0):
    return reduce(lambda x, y: x * y, map(int, lst0))


