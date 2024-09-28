dict0 = {'a': [1, 2, 3], 'b': [1, 2], 'c': [1]}
expected_result =  {'c': [1], 'b': [1, 2], 'a': [1, 2, 3]}
assert test(dict0) == expected_result, 'Test failed'