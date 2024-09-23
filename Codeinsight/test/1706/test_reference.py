def test(lst0, lst1):
    zipped_lists = zip(lst0, lst1)
    sorted_pairs = sorted(zipped_lists, key=lambda x: x[0])
    sorted_lst0, sorted_lst1 = zip(*sorted_pairs)
    return sorted_lst0, sorted_lst1
