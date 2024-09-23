def test(dict0, dict1):
    dict0_copy = dict0.copy()
    dict0_copy.update(dict1)
    return dict0_copy
