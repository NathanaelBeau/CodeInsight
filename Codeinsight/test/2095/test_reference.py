def test(lst0, lst1):
    result_dict = {}
    for i in range(len(lst0)):
        if i < len(lst1):
            result_dict[lst0[i]] = lst1[i]
        else:
            result_dict[lst0[i]] = None
    return result_dict

