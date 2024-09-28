def test(lst0, lst1):
    return [item for item, flag in zip(lst0, lst1) if flag]
