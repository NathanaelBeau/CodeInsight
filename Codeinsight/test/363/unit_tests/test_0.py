df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 6, 7, 8, 9]})
var0 = 'A'
var1 = 5
var2 = 'B'
expected_result =  pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 6, 7, 8, 5]})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'