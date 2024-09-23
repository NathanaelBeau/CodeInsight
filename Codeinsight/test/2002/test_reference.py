def test(dict0, dict1):
    result = {}
    for k, v in dict0.items():
        result[k] = dict1.get(v)
    return result

