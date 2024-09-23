def test(lst0):
    return [(x, y) for x, y in zip(lst0[:-1], lst0[1:]) if y == 9]

