import operator

def test(lst0, index):
    get_items = operator.itemgetter(*index)
    return list(get_items(lst0))

