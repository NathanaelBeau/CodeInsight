def test(lst0, lst1, lst2):
    for i in range(len(lst0)):
        lst2.append((lst0[i][0] + lst1[i][0], lst0[i][1] + lst1[i][1]))
    return lst2

