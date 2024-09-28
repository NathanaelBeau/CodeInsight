df0 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
var0 = 'B'
expected_result =  pd.DataFrame({'A': [7, 8, 9], 'B': [np.nan, 10, 11]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'