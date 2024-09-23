def test(dict0):
    return max(dict0, key=lambda x: dict0[x]['count'])
