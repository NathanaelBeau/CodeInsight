dict0 = {'dict1': {}, 'dict2': {'x': 10}}
expected_result =  [[], ['x']]
assert test(dict0) == expected_result, 'Test failed'