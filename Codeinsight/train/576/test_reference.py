import collections

def test(str0):
    return collections.Counter(str0).most_common(1)[0]

