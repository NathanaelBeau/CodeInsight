def test(lst0):
    tmp = {}
    numbers = []

    [tmp.setdefault(name, len(tmp)) for name in lst0]
    numbers = [tmp[name] for name in lst0]

    return numbers

