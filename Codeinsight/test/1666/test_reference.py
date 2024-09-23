def search_generator(var0, dct0):
    if var0 in dct0:
        yield dct0[var0]
    for value in dct0.values():
        if isinstance(value, dict):
            yield from search_generator(var0, value)

def test(var0, dct0):
    return next(search_generator(var0, dct0), None)
