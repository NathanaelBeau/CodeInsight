def test(lst0):
    return all(sub_list.count(1) == 3 for sub_list in lst0)
