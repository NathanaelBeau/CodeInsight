df0 = pd.DataFrame({'A': [1, 2, np.inf], 'B': [-np.inf, 5, 6]})
expected_result =  pd.DataFrame({'A': [1, 2, np.nan], 'B': [np.nan, 5, 6]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'