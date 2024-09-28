# Test 1
df0 = pd.DataFrame({ 'A': [10, 20, 30], 'B': [40, 50, 60] })
var0 = 'A'
expected_result =  10
result = test(df0, var0)
assert result == expected_result, 'Test failed'