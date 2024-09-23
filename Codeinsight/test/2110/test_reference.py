import operator

def test(var0, lst0):
    return [*map(operator.itemgetter(var0), lst0)]