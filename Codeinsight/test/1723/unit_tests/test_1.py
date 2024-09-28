# Test 2
df0 = pd.DataFrame({'X': ['a', 'b'], 'Y': ['c', 'd']})
var0 = 'list'
expected_result =  {'X': ['a', 'b'], 'Y': ['c', 'd']}
result = test(df0, var0)
assert result == expected_result, 'Test failed'