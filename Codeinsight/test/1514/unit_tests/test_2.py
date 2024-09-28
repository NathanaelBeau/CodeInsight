# Test 1
df0 = pd.DataFrame({'A': [1, ' ', 3], 'B': [4, '    ', 6]})
expected_result =  pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, np.nan, 6]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'