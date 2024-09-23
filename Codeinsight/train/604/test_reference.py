from collections import Counter

def test(lst0):
    counts = Counter(lst0)
    return [k for k in lst0 if counts[k] == 1]


