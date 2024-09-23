def test(arr0, val0):
    for i, row in enumerate(arr0):
        if val0 in row:
            j = row.index(val0)
            return (i, j)
    return None

