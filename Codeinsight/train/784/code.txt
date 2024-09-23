def test(tuple0, tuple1):
    return all(i in tuple1 for i in tuple0)
