
def test(var1):
    if not isinstance(var1, str):
        raise TypeError
    return functools.reduce(lambda x, y: x if ord(x) > ord(y) else y, var1)