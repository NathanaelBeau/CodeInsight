def test(lst0):
    from collections import Counter
    counts = Counter(lst0)
    return [item for item in lst0 if counts[item] == 1]

