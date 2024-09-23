df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [1, 2, 2]})
var0 = 'A'
var1 = 'B'
expected_result =  pd.Series([True, True, False])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'