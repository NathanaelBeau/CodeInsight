def test(dict0):
    return sorted(dict0, key=lambda k: len(dict0[k]), reverse=True)
