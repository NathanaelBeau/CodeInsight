def test(lst0):
    for rowInd, x in enumerate(lst0):
        for colInd, y in enumerate(x):
            lst0[rowInd][colInd] = y + y
    return lst0
