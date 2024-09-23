def test(lst0, lst1):
    return [x for pair in zip(lst0, reversed(lst1)) for x in pair]

