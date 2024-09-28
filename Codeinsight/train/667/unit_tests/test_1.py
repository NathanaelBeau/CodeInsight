dict0 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
expected_result =  [{'a': 1, 'b': 4, 'c': 7}, {'a': 2, 'b': 5, 'c': 8}, {'a': 3, 'b': 6, 'c': 9}]
result = test(dict0)
assert result == expected_result, 'Test failed'