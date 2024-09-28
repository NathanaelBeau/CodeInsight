def test(lst0):
    total = 0
    for sublist in lst0:
        for item in sublist:
            total += item
    return total
