def test(dict0):
    max_key = None
    max_value = float('-inf')
    for key, subdict in dict0.items():
        if subdict['count'] > max_value:
            max_value = subdict['count']
            max_key = key
    return max_key

