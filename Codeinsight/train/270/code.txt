def test(dict0):
    return ''.join('{}{}'.format(key, val) for key, val in dict0.items())
