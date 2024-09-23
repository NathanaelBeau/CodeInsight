# Unit Test 1
df0 = pd.DataFrame({ 'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8] })
var0 = 'A'
var1 = 3
expected_result =  pd.DataFrame({ 'A': [1, 2, 4], 'B': [5, 6, 8] })
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'