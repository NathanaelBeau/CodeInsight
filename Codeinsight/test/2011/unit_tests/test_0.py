var0 = 'A'
var1 = 2
var2 = 'B'
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 2, 6]})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'