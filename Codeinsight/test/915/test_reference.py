import operator

def test(lst0, var0):
    return list(zip(*sorted(enumerate(lst0), key=operator.itemgetter(1))))[0][-var0:]
