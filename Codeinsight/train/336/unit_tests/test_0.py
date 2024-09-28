# Test 1
df0 = pd.DataFrame({ 'A': ['x', 'y', 'x', 'z', 'y'] })
var0 = 'A'
var1 = 'x'
expected_result =  [0, 2]
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'