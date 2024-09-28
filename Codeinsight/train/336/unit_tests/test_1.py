# Test 2
df0 = pd.DataFrame({ 'Scores': [90, 85, 90, 78, 78, 78] })
var0 = 'Scores'
var1 = 78
expected_result =  [3, 4, 5]
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'