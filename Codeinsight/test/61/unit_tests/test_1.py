# Test 2
df0 = pd.DataFrame({'X': [10], 'Y': [20], 'Z': [30]})
var0 = 'X'
expected_result =  0
result = test(df0, var0)
assert result == expected_result, 'Test failed'