def test(lst0, lst1):
    merged_list = []
    for x, y in zip(lst0, lst1):
        if isinstance(x, list):
            merged_list.append(x + y)
        else:
            merged_list.append([x] + y)
    return merged_list