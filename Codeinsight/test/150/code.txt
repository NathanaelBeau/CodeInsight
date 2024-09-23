def test(lst0, lst1):
    return sorted(lst0, key=lambda x: lst1.index(x) if x in lst1 else len(lst1))
