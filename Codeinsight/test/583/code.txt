def test(lst0, lst1):
    return [x for _, x in sorted(zip(lst1, lst0))]
