def test(lst0):
    return [dict(t) for t in {tuple(d.items()) for d in lst0}]
