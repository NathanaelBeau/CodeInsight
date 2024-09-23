import operator

def test(lst0):
    return max(lst0, key=operator.itemgetter(1))