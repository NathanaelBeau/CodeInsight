from collections import ChainMap

def test(lst0):
    return dict(ChainMap(*reversed(lst0)))
