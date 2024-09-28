def test(lst0, lst1, lst2):
    for pair1, pair2 in zip(lst0, lst1):
        lst2.append((pair1[0]+pair2[0], pair1[1]+pair2[1]))
    return lst2
