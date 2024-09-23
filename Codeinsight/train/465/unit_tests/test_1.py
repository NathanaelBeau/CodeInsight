# Test 2
df0 = pd.DataFrame({ 'A': [10, 20, 30], 'B': [40, 50, 60] })
var0 = 'B'
expected_result =  40
result = test(df0, var0)
assert result == expected_result, 'Test failed'