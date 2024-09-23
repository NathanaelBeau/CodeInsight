def test(lst0):
    sorted_list = sorted(lst0)
    return sorted_list == list(range(sorted_list[0], sorted_list[-1]+1))
