dict0 = {'dict1': {'a': 1, 'b': 2}, 'dict2': {'x': 10, 'y': 20}}
expected_result =  [['a', 'b'], ['x', 'y']]
assert test(dict0) == expected_result, 'Test failed'