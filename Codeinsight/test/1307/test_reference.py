def test(lists, selector):
    its = [iter(l) for l in lists]
    for i in selector:
        yield next(its[i])
