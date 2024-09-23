def test(lst0):
    if lst0 and isinstance(lst0[0], tuple):
        return [(x[1], x[0], *x[2:]) for x in lst0]
    else:
        return [[x[1], x[0], *x[2:]] for x in lst0]

