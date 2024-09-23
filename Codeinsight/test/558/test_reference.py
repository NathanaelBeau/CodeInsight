from operator import itemgetter

def test(lst0, lst1):
    return list(itemgetter(*lst1)(lst0))