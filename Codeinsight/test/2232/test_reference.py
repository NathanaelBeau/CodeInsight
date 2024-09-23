def test(dict0, str0):
    return {k: v for k, v in dict0.items() if str0 in k}

