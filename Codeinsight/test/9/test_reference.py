def test(dict0, dict1):
    return {k: dict1.get(v) for k, v in dict0.items()}

