from functools import partial
def test(lst0):
    return list(map(partial(str.split), lst0))