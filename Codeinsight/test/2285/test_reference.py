from itertools import groupby

def test(lst0):
    return {k: list(v) for k, v in groupby(sorted(lst0), key=lambda x: x[0])}
