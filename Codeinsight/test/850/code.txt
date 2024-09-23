import itertools

def test(lst0):
    return sum([i*j for i, j in list(itertools.combinations(lst0, 2))])
