def test(lst0):
    for row in lst0:
        for i in range(len(row)):
            row.insert(i * 2, 0)
    return lst0
