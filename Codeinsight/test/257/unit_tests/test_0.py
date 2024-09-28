df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
var0 = 1
var1 = 1
var2 = 10
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 10, 6]})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'