def test(lst0):
    n = len(lst0)
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst0[i]) > len(lst0[j]):
                temp = lst0[i]
                lst0[i] = lst0[j]
                lst0[j] = temp
    return lst0
