def test(dict0, dict1):
    return {k: dict0[k] / dict1[k] for k in dict0}
