from operator import itemgetter
from itertools import groupby

def test(lst0):
    key = itemgetter(0)
    lst0.sort(key=key)
    result_dict = {}
    for k, group in groupby(lst0, key=key):
        result_dict[k] = [item[1] for item in group]
    return result_dict
