def test(dict0, lst0):
    lst_set = set(lst0)
    return [key for key, value in dict0.items() if lst_set.intersection(value)]
