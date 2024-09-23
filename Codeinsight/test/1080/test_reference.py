def test(lst0, typ0):
    return all(isinstance(x, typ0) for x in lst0)

