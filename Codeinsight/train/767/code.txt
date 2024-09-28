def test(str0):
    it = iter(str0)
    return ''.join(next(it, '') + c for c in it)
