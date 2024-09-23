def test(lst0, lst1):
    for x in range(4):  
        lst0[x].append(lst1[x])
    return lst0