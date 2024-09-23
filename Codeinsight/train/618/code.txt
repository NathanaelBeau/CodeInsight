from collections import defaultdict

def test(lst0, var0, var1):
    d = defaultdict(list)
    for i in lst0:
        for j in range(int(i), int(i) + var1):
            d[j].append(var0)
    return d
