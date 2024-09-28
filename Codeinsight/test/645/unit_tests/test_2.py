df0 = pd.DataFrame({'E': [np.nan, np.nan, np.nan, 4], 'F': [5, 6, 7, 8]})
var0 = 'E'
expected_result =  pd.DataFrame({'E': [np.nan, np.nan, np.nan], 'F': [5, 6, 7]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'