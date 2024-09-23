def test(lst0):
    return [sum(list(zip(*x))[1]) if x else 0 for x in lst0]
