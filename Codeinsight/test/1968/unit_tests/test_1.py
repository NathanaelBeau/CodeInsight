var0 = 'C'
var1 = 'D'
new_value = 20
df0 = pd.DataFrame({'C': [2, 4, 6], 'D': [7, 8, 9]})
expected_result =  pd.DataFrame({'C': [2, 4, 6], 'D': [7, 20, 20]})
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'