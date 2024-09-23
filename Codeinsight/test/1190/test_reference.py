import functools

def test(lst0):
    return functools.reduce(lambda x, y: x + list(y), lst0, [])
