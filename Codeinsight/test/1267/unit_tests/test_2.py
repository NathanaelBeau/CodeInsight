# Test 3
df0 = pd.DataFrame({'M': [10, 11, 12], 'N': [13, 14, 15], 'O': [16, 17, 18]})
lst0 = ['M', 'O']
expected_result =  pd.DataFrame({'M': [10, 11, 12], 'O': [16, 17, 18]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'