# Test 3
df0 = pd.DataFrame({'M': [10.01, 11.49, 12.99]})
var0 = 'N'
var1 = 13.50
expected_result =  pd.DataFrame({'M': [10.01, 11.49, 12.99], 'N': [13.50, 13.50, 13.50]})
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'