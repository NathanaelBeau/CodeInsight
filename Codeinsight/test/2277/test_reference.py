def test(lst0, item0):
    index = next((i for i, v in enumerate(lst0) if v[1] > item0[1]), len(lst0))
    lst0.insert(index, item0)
    return lst0

