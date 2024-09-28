# Test 2
df0 = pd.DataFrame({'B': [5.9, 6.4, 7.2, 8.6]})
var0 = 'B'
expected_result =  pd.DataFrame({'B': [5, 6, 7, 8]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'