def test(dict0):
    return sorted(dict0.items(), key=lambda item: (item[1], item[0]))
