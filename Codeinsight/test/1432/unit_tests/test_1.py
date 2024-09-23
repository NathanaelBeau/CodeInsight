# Unit Test 3
df0 = pd.DataFrame({ 'X': ['a', 'b', 'c', 'd'], 'Y': ['e', 'f', 'g', 'h'] })
var0 = 'X'
var1 = 'c'
expected_result =  pd.DataFrame({ 'X': ['a', 'b', 'd'], 'Y': ['e', 'f', 'h'] })
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'