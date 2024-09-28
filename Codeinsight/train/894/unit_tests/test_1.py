# Test 2
df0 = pd.DataFrame({'X': [0.1, 0.5, 0.3], 'Y': [0.2, 0.4, 0.6]})
var0 = 'Y'
expected_result =  pd.Series([0.3, 0.6], name=2, index=['X', 'Y'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'