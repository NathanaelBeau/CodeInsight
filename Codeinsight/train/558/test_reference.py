def test(dict0):
    sorted_items = sorted(dict0.items(), key=lambda x: x[1])
    sorted_items = sorted(sorted_items, key=lambda x: x[0], reverse=True)
    return sorted_items

