df0 = pd.DataFrame({'A': [1, 3, 6, 10]})
var0 = 'A'
expected_result =  pd.DataFrame({'A': [1, 3, 6, 10], 'diff_column': [np.nan, 2, 3, 4]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'