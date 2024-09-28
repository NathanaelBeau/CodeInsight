# Test 3
df0 = pd.DataFrame({ 'X': [1.1, 3.3, 2.2], 'Y': [4.4, 5.5, 6.6] })
var0 = 'Y'
expected_result =  pd.DataFrame({ 'X': [1.1, 3.3, 2.2], 'Y': [4.4, 5.5, 6.6] })
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'