def test(lst0):
    return max(max(sublist, key=lambda x: x[1])[1] for sublist in lst0)

