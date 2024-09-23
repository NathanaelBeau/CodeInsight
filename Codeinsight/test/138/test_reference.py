def test(dict0):
    return dict((k.lower(), v.lower()) for k, v in dict0.items())
