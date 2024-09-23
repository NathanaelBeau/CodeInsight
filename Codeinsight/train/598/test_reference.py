def test(lst0, var0):
    from collections import Counter
    return Counter(map(type, lst0))[var0]
