def test(dict0, dict1):
    result = {}
    for key in dict1:
        values_in_dict0 = dict0.get(key, [])
        values_in_dict1 = dict1[key]
        common_values = list(set(values_in_dict0).intersection(values_in_dict1))
        result[key] = common_values
    return result

