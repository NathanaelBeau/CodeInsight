# Unit Test 2
df0 = pd.DataFrame({ 'X': [10, 11, 12], 'Y': [13, 14, 15], 'Z': [16, 17, 18] })
var0 = 'X'
expected_result =  pd.DataFrame({ 'Y': [13, 14, 15], 'Z': [16, 17, 18] })
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'