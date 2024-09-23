import collections
def test(lst0):
    return [item for item, count in collections.Counter(lst0).items() if count > 1]

