def test(lst0, lst1):
    return [int(i == j) for i, j in zip(lst0, lst1)]
