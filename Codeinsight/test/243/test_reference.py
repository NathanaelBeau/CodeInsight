def test(lst0, lst1):
    return [item for item in lst0 if item[0] in [x[0] for x in lst1]]
