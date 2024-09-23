def test(str0):
    return ''.join([str0[i+1] + str0[i] if i+1 < len(str0) else str0[i] for i in range(0, len(str0), 2)])
