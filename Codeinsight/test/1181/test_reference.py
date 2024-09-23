def test(lst0, var0):
    return [(x, y) for x, y in zip(lst0, lst0[1:]) if y == var0]

