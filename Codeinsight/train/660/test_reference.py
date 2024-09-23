def test(lst0, lst1):
    return sum(lst0[i] * lst1[i] for i in range(len(lst0)))

