def test(lst0, lst1):
    total = 0
    for item0, item1 in zip(lst0, lst1):
        total += item0 * item1
    return total
