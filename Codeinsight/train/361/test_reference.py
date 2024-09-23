from itertools import groupby

def test(lst0):
    return [key for key, group in groupby(lst0)]
