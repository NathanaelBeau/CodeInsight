from functools import reduce

def test(lst0):
    return reduce(lambda x, y: 10 * x + y, lst0)

