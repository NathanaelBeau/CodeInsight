from collections import Counter

def test(lst0):
    result = Counter()
    for d in lst0:
        result.update(d)
    return dict(result.most_common())
