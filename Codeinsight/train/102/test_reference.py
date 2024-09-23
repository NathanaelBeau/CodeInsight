def test(lst1, lst2): 
    return all(map(lst1.__contains__, lst2))
