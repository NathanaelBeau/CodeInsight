# Test 2
df0 = pd.DataFrame({ 'X': ['a', 'b', 'c'] })
var0 = 'Y'
lst0 = ['d', 'e', 'f']
expected_result =  pd.DataFrame({ 'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f'] })
assert test(df0.copy(), var0, lst0).equals(expected_result), 'Test failed'