from itertools import groupby

def test(lst0):
    lst0.sort(key=lambda x: x[0])
    grouped = [next(group) for _, group in groupby(lst0, key=lambda x: x[0])]
    return grouped

