def test(lst0):
    unique_items = []
    for item in lst0:
        if item not in unique_items:
            unique_items.append(item)
    unique_items.sort()
    return unique_items
