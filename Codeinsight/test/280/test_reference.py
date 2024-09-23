def test(str0, lst0):
    return [str0[i:j] for i, j in zip([0]+lst0, lst0+[None])]
