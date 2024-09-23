df0 = pd.DataFrame({'C': [1, 2, 3, 4], 'D': [np.nan, 6, np.nan, 8]})
var0 = 'D'
expected_result =  pd.DataFrame({'C': [1, 3], 'D': [np.nan, np.nan]}, index=[0, 2])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'