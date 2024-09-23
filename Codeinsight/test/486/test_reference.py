from itertools import islice

def test(lst0, var0, var1):
    return list(islice(lst0, var0, var1))
