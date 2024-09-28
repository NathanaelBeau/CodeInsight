def test(dict0, var0):
    return {key: val for key, val in dict0.items() if val != var0}
