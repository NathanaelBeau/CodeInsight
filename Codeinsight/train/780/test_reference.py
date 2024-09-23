def test(str0):
    return ''.join([str0[i+1] + str0[i] for i in range(0, len(str0)-1, 2)]) + (str0[-1] if len(str0) % 2 else '')

