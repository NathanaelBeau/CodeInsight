def test(dict0):
    result = []
    for k, v in dict0.items():
        result.extend([k] * v)
    return result

