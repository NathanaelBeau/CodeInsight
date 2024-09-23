import itertools

def test(lst0):
    return list(itertools.product(*lst0))
