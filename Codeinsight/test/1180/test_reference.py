def test(dict0, dict1):
    result = {}
    for key, value in dict0.items():
        result[key] = dict1[value]
    return result

