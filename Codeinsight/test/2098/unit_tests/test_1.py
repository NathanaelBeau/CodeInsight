# Test 2 (row extraction)
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
var0 = 1
var1 = 'row'
expected_result =  [2, 5]
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'