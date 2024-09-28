from itertools import islice

def test(lst0, var0):
    it = iter(lst0)
    return [list(islice(it, var0)) for _ in range(0, len(lst0), var0)]
