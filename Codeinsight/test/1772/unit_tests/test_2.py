df0 = pd.DataFrame({'M': [7], 'N': [8], 'O': [9]})
var0 = 0
expected_result =  pd.Series([7], name='M')
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'