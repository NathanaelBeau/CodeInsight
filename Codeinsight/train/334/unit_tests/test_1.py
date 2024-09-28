# Unit Test 2
dict0 = {'X': [7, 8, 9], 'Y': [10, 11, 12]}
expected_result =  pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 11, 12]})
result = test(dict0)
assert result.equals(expected_result), 'Test failed'