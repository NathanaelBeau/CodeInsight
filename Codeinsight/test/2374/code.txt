from operator import itemgetter
def test(lst0):
    return list(map(itemgetter(0), lst0))