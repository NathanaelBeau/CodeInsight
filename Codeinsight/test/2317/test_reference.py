import itertools

def test(lst0, var0):
    return [list(g) for k, g in itertools.groupby(lst0, lambda x: x in var0) if not k]
