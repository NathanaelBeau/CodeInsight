def test(dict0, dict1):
    return {k: dict0[k] for k in dict0.keys() & dict1.keys()}