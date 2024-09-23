# Test 1
df0 = pd.DataFrame({'A': [np.nan, 2., np.nan, 4., 5.]})
expected_result =  pd.DataFrame({'A': [np.nan, 2., 2., 4., 5.]})
result = test(df0.copy(), 'ffill')
assert result.equals(expected_result), 'Test failed'