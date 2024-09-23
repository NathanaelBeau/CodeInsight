from functools import reduce

def test(lst0):
    return [reduce(lambda x, y: x + y, i) for i in lst0]
