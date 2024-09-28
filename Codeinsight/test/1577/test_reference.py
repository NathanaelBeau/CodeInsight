def test(lst0):
    return {k: v for k, v in (e.split(':') for e in lst0)}
