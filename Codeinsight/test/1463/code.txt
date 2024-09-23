def test(dict0):
    result = {}
    for key, value in dict0.items():
        result.setdefault(value, []).append(key)
    return {key: value for key, value in result.items() if len(value) > 1}
