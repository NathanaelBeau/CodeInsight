def test(lst0, lst1):
    return sum(1 for i, j in zip(lst0, lst1) if i != j)

