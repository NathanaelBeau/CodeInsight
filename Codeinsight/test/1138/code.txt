def test(lst0):
    reversed_tuples = [tuple(x[::-1]) for x in lst0]
    return tuple(reversed_tuples)
