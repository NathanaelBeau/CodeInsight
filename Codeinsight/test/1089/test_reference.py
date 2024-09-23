def test(lst0, lst1):
    return [item for item in lst0 if any(x in item for x in lst1)]

