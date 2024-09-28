var0 = 'X'
var1 = 'Y'
new_value = 30
df0 = pd.DataFrame({'X': [0, 2, 4], 'Y': [10, 11, 12]})
expected_result =  pd.DataFrame({'X': [0, 2, 4], 'Y': [10, 11, 30]})
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'