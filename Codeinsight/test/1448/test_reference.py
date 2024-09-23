def test(lst0):
    return sorted(set([item for sublist in lst0 for item in sublist]))

