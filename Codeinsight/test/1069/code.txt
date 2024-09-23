def test(lst0):
    if len(lst0) == 2:  
        return [(i, j) for i in lst0[0] for j in lst0[1]]
