# Unit Test 1
dict0 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = test(dict0)
assert result.equals(expected_result), 'Test failed'