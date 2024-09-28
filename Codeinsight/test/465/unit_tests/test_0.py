# Test 1
df0 = pd.DataFrame({ 'A': [1, 2, 3] })
var0 = 'B'
expected_result =  pd.DataFrame({ 'A': [1, 2, 3], 'B': [None, None, None] })
result = test(df0.copy(), var0)
assert result.equals(expected_result), 'Test failed'