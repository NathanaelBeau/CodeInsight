def test(lst0, lst1):
    return sum(x * y for x, y in zip(lst0, lst1))
