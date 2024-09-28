dict0 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
expected_result =  {'c': [7, 8, 9], 'b': [4, 5, 6], 'a': [1, 2, 3]}
result = test(dict0)
assert result == expected_result, 'Test failed'