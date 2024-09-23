import operator

def test(lst0):
    f = operator.itemgetter(1)
    return [sum(map(f, x)) for x in lst0]
