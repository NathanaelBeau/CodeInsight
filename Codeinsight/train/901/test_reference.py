import operator

def test(var0, var1):
    return [*map(operator.itemgetter(var0), var1)]
