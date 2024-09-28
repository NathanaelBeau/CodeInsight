import operator

def test(lst0, var0):
    return sorted(lst0, key=operator.itemgetter(var0))