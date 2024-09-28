df0 = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
expected_result =  pd.DataFrame({'A': [1., 2., np.nan], 'B': [4., np.nan, 6.]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'