def test(lst0, lst1):
    for i in lst0:
        while i in lst1:
            lst1.remove(i)
    return lst1
