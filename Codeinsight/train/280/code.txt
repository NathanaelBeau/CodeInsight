import operator

def test(lst0, var0, var1):
    return sorted(lst0, key=operator.itemgetter(var0, var1))
