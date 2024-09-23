def test(lst0, lst1):
    return [index for index, item in enumerate(lst0) if item in lst1]
