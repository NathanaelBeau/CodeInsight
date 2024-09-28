# Test 2
df0 = pd.DataFrame({'A': [1, np.nan, 3., np.nan, np.nan]})
expected_result =  pd.DataFrame({'A': [1., 3., 3., np.nan, np.nan]})
result = test(df0.copy(), 'bfill')
assert result.equals(expected_result), 'Test failed'