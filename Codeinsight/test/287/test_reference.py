def test(lst0):
    d = {}
    for x, y, z in lst0:
        d[x] = d.get(x, 0) + 1
    return d

