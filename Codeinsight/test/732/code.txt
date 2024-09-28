def test(dict0):
    new_dict = {}
    for k, v in dict0.items():
        new_dict[k.lower()] = v.lower()
    return new_dict