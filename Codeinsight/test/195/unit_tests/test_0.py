# Test 1
df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
var0 = 1
var1 = 'X'
var2 = [5, 6]
expected_result =  pd.DataFrame({'A': [1, 2], 'X': [5, 6], 'B': [3, 4]})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'