def test(dict0, dict1):
    return {key: dict0[key] - dict1.get(key, 0) for key in dict0}

