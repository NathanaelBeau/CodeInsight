def test(dct0):
    return dict(sorted(dct0.items(), key=lambda item: max(item[1]), reverse=True))

