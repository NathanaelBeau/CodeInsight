import collections

def test(lst0):
    freq = collections.Counter(lst0)
    return sorted(lst0, key=lambda x: (-freq[x], x))

