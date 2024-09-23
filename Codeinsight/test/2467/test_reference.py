from collections import Counter

def test(lst0, lst1):
    return dict(Counter(lst0) - Counter(lst1))

