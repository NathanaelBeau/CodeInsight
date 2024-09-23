def test(var1):
    c = collections.Counter(var1)
    return c.most_common(1)
