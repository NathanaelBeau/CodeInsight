def test(lst0):
    return max(len(s) for sublist in lst0 for s in sublist)
