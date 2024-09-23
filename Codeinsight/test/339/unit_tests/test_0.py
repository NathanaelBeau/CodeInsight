df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
var0 = 0
var1 = 'X'
expected_result =  pd.DataFrame({'X': [1, 2, 3], 'B': [4, 5, 6]})
result = test(df0.copy(), var0, var1)
assert result.equals(expected_result), 'Test failed'