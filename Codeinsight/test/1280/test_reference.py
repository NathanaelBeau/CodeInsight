import operator

def test(lst0, lst1):
    sorted_lists = sorted(zip(lst0, lst1), key=operator.itemgetter(0), reverse=True)
    list_0_sorted, list_1_sorted = zip(*sorted_lists)
    return list(list_0_sorted), list(list_1_sorted)

