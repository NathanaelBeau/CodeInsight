from itertools import takewhile

def test(lst0):
    return list(takewhile(lambda x: lst0.index(x) < 10, lst0))
