df0 = pd.DataFrame({ 'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f'], 'Z': ['g', 'h', 'i'] })
var0 = 'Z'
expected_result =  pd.DataFrame({ 'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f'] })
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'