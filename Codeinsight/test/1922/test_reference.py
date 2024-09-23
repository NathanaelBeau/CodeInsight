def test(lst0, lst1):
    return [1 if i == j else 0 for i, j in zip(lst0, lst1)]

