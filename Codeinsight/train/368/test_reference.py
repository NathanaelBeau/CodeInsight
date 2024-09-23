def test(lst0, lst1):
    return [a is b for a, b in zip(lst0, lst1)]

