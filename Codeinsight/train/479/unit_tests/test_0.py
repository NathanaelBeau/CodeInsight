# Test 1
df0 = pd.DataFrame({'A': [1., np.nan, 3.], 'B': [4., 5., np.nan], 'C': [7., 8., 9.]})
expected_result =  pd.DataFrame({'A': [1., 0., 3.], 'B': [4., 5., 0.], 'C': [7., 8., 9.]})
result = test(df0, ['A', 'B'], 0)
assert result.equals(expected_result), 'Test failed'