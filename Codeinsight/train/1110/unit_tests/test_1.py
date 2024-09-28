# Unit Test 3
df0 = pd.DataFrame({ 'X': ['a', 'b', 'c', 'd'], 'Y': ['e', 'f', 'g', 'h'] })
var0 = 'Z'
expected_result =  False
result = test(df0, var0)
assert result == expected_result, 'Test failed'