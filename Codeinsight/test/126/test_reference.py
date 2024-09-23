def test(str0, lst0):
    slicer = lambda s: lst0[int(s.split(':')[0]):int(s.split(':')[1])]
    return slicer(str0)

