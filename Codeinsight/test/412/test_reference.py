def test(lst0, lst1):
    common_indices = []
    for i, item in enumerate(lst0):
        if item in lst1:
            common_indices.append(i)
    return common_indices

