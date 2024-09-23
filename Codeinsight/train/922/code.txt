def test(str0, char0):
    return ''.join([str0[i:i+2] + char0 for i in range(0, len(str0), 2)])[:-1]
