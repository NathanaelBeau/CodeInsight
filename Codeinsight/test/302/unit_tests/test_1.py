# Test 2
df0 = pd.DataFrame({ 'apple': [10, 20, 30] })
var0 = 'banana'
expected_result =  pd.DataFrame({ 'apple': [10, 20, 30], 'banana': [None, None, None] })
result = test(df0.copy(), var0)
assert result.equals(expected_result), 'Test failed'