dict0 = {'x': [10], 'y': [10, 20], 'z': [10, 20, 30]}
expected_result =  {'x': [10], 'y': [10, 20], 'z': [10, 20, 30]}
assert test(dict0) == expected_result, 'Test failed'