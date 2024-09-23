from collections import Counter

def test(lst0):
    c = Counter(lst0)
    value, count = c.most_common()[0]
    return value, count

