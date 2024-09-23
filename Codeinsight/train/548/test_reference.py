def test(lst0, lst1):
    list_common = []
    for a in lst0:
        if a in lst1:
            list_common.append(a)
    return list_common

