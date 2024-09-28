def test(lst0):
    return all(isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], int) and isinstance(item[1], int) for item in lst0)
