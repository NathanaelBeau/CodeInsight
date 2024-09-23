import collections

def test(str0):
    d = collections.defaultdict(int)
    for c in str0:
        d[c] += 1
    return sorted(d.items(), key=lambda x: x[1], reverse=True)[0]
