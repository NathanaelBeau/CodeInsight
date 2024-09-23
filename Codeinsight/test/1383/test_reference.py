def test(dict0):
    return max(dict0, key=lambda k: dict0[k]['count'])

