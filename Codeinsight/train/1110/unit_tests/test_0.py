# Unit Test 1
df0 = pd.DataFrame({ 'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8] })
var0 = 'A'
expected_result =  True
result = test(df0, var0)
assert result == expected_result, 'Test failed'