# Test 3 (column extraction again)
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
var0 = 'B'
var1 = 'column'
expected_result =  [4, 5, 6]
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'