# Test 2
df0 = pd.DataFrame({ 'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f'], 'Z': ['g', 'h', 'i'] })
var0 = 'Z'
expected_result =  pd.DataFrame({ 'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f'] })
assert test(df0.copy(), var0).equals(expected_result), 'Test failed'