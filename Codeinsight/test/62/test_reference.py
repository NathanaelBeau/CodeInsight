def test(dict0, dict1):
    return {key: dict0[key] / dict1[key] for key in dict0 if key in dict1}

