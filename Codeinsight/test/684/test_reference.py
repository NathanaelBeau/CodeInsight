import operator

def test(lst0):
    return sorted(lst0, key=operator.itemgetter(2))