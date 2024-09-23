def test(lst0):
    if lst0 and isinstance(lst0[0], tuple):
        return list(map(lambda x: (x[1], x[0], *x[2:]), lst0))
    else:
        return list(map(lambda x: [x[1], x[0], *x[2:]], lst0))
