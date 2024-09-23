def test(dct0):
    return sum(1 for key, value in dct0.items() if key == 'success' and value == True)

