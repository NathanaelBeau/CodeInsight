from operator import attrgetter

def test(lst0, var0):
    return sorted(lst0, key=attrgetter(var0), reverse=True)