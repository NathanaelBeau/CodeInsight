# Test 1
df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
var0 = 'B'
expected_result =  1
result = test(df0, var0)
assert result == expected_result, 'Test failed'