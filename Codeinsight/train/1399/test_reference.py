from operator import itemgetter

def test(lst0, var0):
    return sorted(lst0, key=itemgetter(var0))