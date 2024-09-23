def test(arr0, var0):
    return np.array([arr0[i:i+var0] for i in range(len(arr0) - var0 + 1)])

