df0 = pd.DataFrame({'E': [13, 14, 15], 'F': [16, 17, 18]})
var0 = 1
var1 = 'Z'
expected_result =  pd.DataFrame({'E': [13, 14, 15], 'Z': [16, 17, 18]})
result = test(df0.copy(), var0, var1)
assert result.equals(expected_result), 'Test failed'