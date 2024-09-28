import collections

def test(lst0):
    return sorted(lst0, key=lambda x: (-collections.Counter(lst0)[x], x))
