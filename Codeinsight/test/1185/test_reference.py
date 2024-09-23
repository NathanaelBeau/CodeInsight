def test(lst0, lst1):
    common_elements = set(lst0) & set(lst1)
    return [index for index, item in enumerate(lst0) if item in common_elements]

