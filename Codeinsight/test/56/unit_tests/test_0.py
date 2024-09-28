# Test 1 (column extraction)
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
var0 = 'A'
var1 = 'column'
expected_result =  [1, 2, 3]
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'