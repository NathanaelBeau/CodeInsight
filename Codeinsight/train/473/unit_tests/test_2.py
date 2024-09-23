# Test 3
df0 = pd.DataFrame({'C': [10.01, 11.49, 12.99, 13.50]})
var0 = 'C'
expected_result =  pd.DataFrame({'C': [10, 11, 12, 13]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'