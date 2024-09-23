def test(dict0, dict1):
    return dict((k, dict0[k]) for k in dict0 if k in dict1)