def test(lst0, lst1):
    return [i == j for i, j in zip(lst0, lst1)]
