df0 = pd.DataFrame({'B': [5, 7, 6, 4]})
var0 = 'B'
expected_result =  pd.DataFrame({'B': [5, 7, 6, 4], 'diff_column': [np.nan, 2, -1, -2]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'