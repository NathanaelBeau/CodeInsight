var0 = 'A'
var1 = 2
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [2, 4, 6], 'B': [4, 5, 6]})
result = test(df0.copy(), var0, var1)
assert result.equals(expected_result), 'Test failed'