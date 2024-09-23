def test(dict0, dict1):
    return {key: dict1[value] for key, value in dict0.items()}
