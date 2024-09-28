from itertools import chain

def test(lst0):
    return {k for k in chain(*lst0)}