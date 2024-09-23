# Test 3
df0 = pd.DataFrame({'A': [np.nan, np.nan, 3., 4., 5.]})
expected_result =  pd.DataFrame({'A': [3., 3., 3., 4., 5.]})
result = test(df0.copy(), 'bfill')
assert result.equals(expected_result), 'Test failed'