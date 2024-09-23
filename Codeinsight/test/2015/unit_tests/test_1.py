# Unit Test 2 for Excluding
df0 = pd.DataFrame({ 'X': [10, 11, 12], 'Y': [13, 14, 15], 'Z': [16, 17, 18] })
lst0 = ['Y']
expected_result_exclude_2 = pd.DataFrame({'X': [10, 11, 12], 'Z': [16, 17, 18]})
result_exclude_2 = test(df0, lst0)
assert result_exclude_2.equals(expected_result_exclude_2), 'Test failed'