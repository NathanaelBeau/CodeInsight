from collections import Counter
def test(var0):
    counts = Counter(var0)
    return sum(1 for count in counts.values() if count > 1)
