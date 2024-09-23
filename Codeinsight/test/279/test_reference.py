def test(lst0, lst1):
    common_elements = []
    for item in lst0:
        if item in lst1:
            common_elements.append(item)
    return set(common_elements)

