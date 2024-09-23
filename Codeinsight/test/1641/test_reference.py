
def test(lst0, var0):
    return [x for x in map(lambda x: x if x > var0 else None, lst0) if x is not None]