def test(lst0):
    for i in lst0:
        if isinstance(i, list):
            yield from test(i)
        else:
            yield i
