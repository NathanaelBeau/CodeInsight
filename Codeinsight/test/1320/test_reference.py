def _itersplit(lst0, var0):
    current = []
    for item in lst0:
        if item in var0:
            yield current
            current = []
        else:
            current.append(item)
    yield current

def test(lst0, var0):
    return [subl for subl in _itersplit(lst0, var0) if subl]

