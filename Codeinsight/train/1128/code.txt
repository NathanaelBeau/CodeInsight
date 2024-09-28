def test(*args):
    return list(map(sum, zip(*args)))
