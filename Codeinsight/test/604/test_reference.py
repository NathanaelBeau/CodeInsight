from itertools import chain

def test(lst0):
    flattened_list = list(chain.from_iterable(lst0))
    return flattened_list

