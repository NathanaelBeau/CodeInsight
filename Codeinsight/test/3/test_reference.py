def test(lst0):
    from collections import Counter
    return Counter(elem[0] for elem in lst0)

