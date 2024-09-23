def test(dict0):
    return sorted(dict0.items(), key=lambda x: (x[1], x[0]), reverse=True)

