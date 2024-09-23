def test(lst0, var0):
    a = [[] for _ in range(lst0)]

    for i in range(lst0):
        a[i].append(var0[i])

    return a

