df0 = pd.DataFrame({'E': [10, 20, 30], 'F': [30, 20, 10]})
var0 = 'E'
var1 = 'F'
expected_result =  pd.Series([False, True, False])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'