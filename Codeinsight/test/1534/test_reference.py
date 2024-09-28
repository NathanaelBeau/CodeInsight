def test(lst0, lst1):
    return [x for _, x in sorted(zip(lst0, lst1), key=lambda pair: pair[0])]
