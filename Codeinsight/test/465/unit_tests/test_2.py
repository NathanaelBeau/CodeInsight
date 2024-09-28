# Test 3
df0 = pd.DataFrame({ 'x': ['a', 'b', 'c'] })
var0 = 'y'
expected_result =  pd.DataFrame({ 'x': ['a', 'b', 'c'], 'y': [None, None, None] })
result = test(df0.copy(), var0)
assert result.equals(expected_result), 'Test failed'