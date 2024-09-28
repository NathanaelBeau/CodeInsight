# Test 2
df0 = pd.DataFrame({'Y': ['a', 'b'], 'Z': ['c', 'd']})
var0 = 0
var1 = 'W'
var2 = ['e', 'f']
expected_result =  pd.DataFrame({'W': ['e', 'f'], 'Y': ['a', 'b'], 'Z': ['c', 'd']})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'