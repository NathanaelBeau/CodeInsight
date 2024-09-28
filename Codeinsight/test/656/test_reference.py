def test(lst0):
    return [all(x == sub_lst[0] for x in sub_lst) for sub_lst in lst0]
