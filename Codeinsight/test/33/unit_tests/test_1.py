var0 = 'B'
var1 = 3
df0 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
expected_result =  pd.DataFrame({'A': [7, 8, 9], 'B': [30, 33, 36]})
result = test(df0.copy(), var0, var1)
assert result.equals(expected_result), 'Test failed'