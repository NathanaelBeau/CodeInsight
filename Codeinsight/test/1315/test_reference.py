def test(lst0, lst1):
    return set(filter(lambda item: item in lst1, lst0))

