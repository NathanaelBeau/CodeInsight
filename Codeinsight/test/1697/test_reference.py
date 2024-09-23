def test(lst0, lst1, lst2, lst3, lst4, lst5):
    length = len(lst0)
    return all(len(lst) == length for lst in [lst1, lst2, lst3, lst4, lst5])
