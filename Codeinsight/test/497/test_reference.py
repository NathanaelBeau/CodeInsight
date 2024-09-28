def test(lst0, lst1):
    result_dict = {}
    for i, key in enumerate(lst0):
        if i < len(lst1):
            result_dict[key] = lst1[i]
        else:
            result_dict[key] = None
    return result_dict
