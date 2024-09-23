def test(str0):
    return [sum(map(int, str0[i:i+2])) for i in range(len(str0)-1)]
