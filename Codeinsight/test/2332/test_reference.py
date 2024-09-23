def test(tuple0, tuple1):
    return tuple(map(sum, zip(tuple0, tuple1)))
