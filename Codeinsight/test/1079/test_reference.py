def test(str0):
    return [int(str0[i:i+3], 2) for i in range(0, len(str0), 3)]

