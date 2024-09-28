from functools import reduce

def test(lst0, var0):
    return reduce(lambda acc, x: acc + ([x] if not var0(x) else []), lst0, [])
