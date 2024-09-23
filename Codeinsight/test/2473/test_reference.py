def test(dict0, var0):
    return [k for k, _ in sorted(dict0.items(), key=lambda item: item[1][var0])]

