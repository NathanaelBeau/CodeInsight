def test(lst0):
    return [''.join(lst0[i:i+2]) for i in range(0, len(lst0), 2)]

