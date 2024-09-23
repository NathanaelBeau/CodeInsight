import itertools
def test(lst0, lst1):
    return list(itertools.compress(lst0, lst1))
