df0 = pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f']})
var0 = 0
var1 = 0
var2 = 'z'
expected_result =  pd.DataFrame({'X': ['z', 'b', 'c'], 'Y': ['d', 'e', 'f']})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'