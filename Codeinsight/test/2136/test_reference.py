from itertools import groupby
import operator

def test(lst0):
    return {k: list(v) for k, v in groupby(sorted(lst0), key=operator.itemgetter(0))}
