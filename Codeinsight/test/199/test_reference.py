def test(dict0, str0, var0):
    if str0 in dict0:
        dict0[str0].append(var0)
    else:
        dict0[str0] = [var0]
    return dict0
