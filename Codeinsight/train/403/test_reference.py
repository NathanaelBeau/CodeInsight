def test(dictA, str0):
    return [k for k, v in dictA.items() if v.count(str0) > 1]
