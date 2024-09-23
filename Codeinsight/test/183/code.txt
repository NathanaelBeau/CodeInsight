def test(arr0, var0, var1):
    return np.pad(arr0, ((0, var0), (0, var1)), 'constant')
