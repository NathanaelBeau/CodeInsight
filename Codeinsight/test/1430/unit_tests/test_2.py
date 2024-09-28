df0 = pd.DataFrame({'C': [10, 10, 10, 10]})
var0 = 'C'
expected_result =  pd.DataFrame({'C': [10, 10, 10, 10], 'diff_column': [np.nan, 0, 0, 0]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'