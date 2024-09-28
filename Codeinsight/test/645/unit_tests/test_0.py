df0 = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, 6, 7, 8]})
var0 = 'A'
expected_result =  pd.DataFrame({'A': [np.nan], 'B': [7]}, index=[2])
result = test(df0, var0)
assert result .equals( expected_result), 'Test failed'