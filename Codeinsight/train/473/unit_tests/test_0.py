# Test 1
df0 = pd.DataFrame({'A': [1.2, 2.8, 3.5, 4.1]})
var0 = 'A'
expected_result =  pd.DataFrame({'A': [1, 2, 3, 4]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'