from itertools import groupby

def test(lst0):
    lst0.sort(key=lambda x: x[:5])
    return [list(g) for k, g in groupby(lst0, key=lambda x: x[:5])]