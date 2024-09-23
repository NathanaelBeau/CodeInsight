def test(dict0):
    result_dict = {}
    for k, v in dict0.items():
        result_dict[k] = int(v)
    return result_dict

