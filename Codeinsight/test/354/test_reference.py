def test(lst0):
    return all(lst0.count(item) == 1 for item in lst0)
