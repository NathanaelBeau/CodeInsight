# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3, 4]})
var0 = 'B'
var1 = 5
expected_result =  pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 5, 5, 5]})
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'