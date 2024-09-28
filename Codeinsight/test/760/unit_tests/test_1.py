# Test 2
df0 = pd.DataFrame({'X': ['a', 'b', 'c']})
var0 = 'Y'
var1 = 'z'
expected_result =  pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['z', 'z', 'z']})
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'