def test(lst0):
    unique_items = []
    for item in lst0:
        if lst0.count(item) == 1:
            unique_items.append(item)
    return unique_items

