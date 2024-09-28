# Test 3
df0 = pd.DataFrame({'M': [10], 'N': [13]})
df1 = pd.DataFrame({'M': [11], 'N': [14]})
expected_result =  pd.DataFrame({'M': [10, 11], 'N': [13, 14]})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'