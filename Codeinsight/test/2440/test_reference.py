def test(lst0):
    unique_list= list(map(list, set(map(lambda i: tuple(i), lst0))))
    sorted_list = sorted(unique_list)
    return sorted_list
