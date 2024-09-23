def test(dct0):
    return dict(sorted(dct0.items(), key=lambda item: item[1][1]))
