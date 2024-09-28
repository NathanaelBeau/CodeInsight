def test(lst0, var0):
    return [(i, j) for i, row in enumerate(lst0) for j, x in enumerate(row) if x == var0]
