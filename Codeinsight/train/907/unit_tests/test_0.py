# Test 1
df0 = pd.DataFrame({'A': [1., 2., np.nan, 6.], 'B': [np.nan, 2, 3, 4]})
expected_result =  pd.DataFrame({'A': [1., 2., 3., 6.], 'B': [3., 2., 3., 4.]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'