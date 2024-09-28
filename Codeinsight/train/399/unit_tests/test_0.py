var0 = 'A'
var1 = 'B'
new_value = 10
df0 = pd.DataFrame({'A': [1, 3, 5], 'B': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [1, 3, 5], 'B': [4, 10, 10]})
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'