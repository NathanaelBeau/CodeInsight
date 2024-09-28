import operator

def test(lst0):
    return tuple(map(operator.itemgetter(0), lst0))
