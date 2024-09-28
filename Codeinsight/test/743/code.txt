def test(dict0):
    return dict(sorted(dict0.items(), key=lambda x: len(x[1])))
