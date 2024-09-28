dict0 = {'first': [7, 8], 'second': [4, 5, 6, 7, 8, 9], 'third': [1, 2, 3, 4, 5, 6, 7]}
expected_result =  {'second': [4, 5, 6, 7, 8, 9], 'third': [1, 2, 3, 4, 5, 6, 7], 'first': [7, 8]}
result = test(dict0)
assert result == expected_result, 'Test failed'