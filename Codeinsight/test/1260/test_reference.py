def test(lst0, lst1):
    combined_lists = list(zip(lst0, lst1))
    combined_lists.sort(key=lambda x: x[0], reverse=True)
    list_0_sorted, list_1_sorted = zip(*combined_lists)
    return list(list_0_sorted), list(list_1_sorted)

