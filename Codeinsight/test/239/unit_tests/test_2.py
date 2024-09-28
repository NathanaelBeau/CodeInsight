# Test 3
df0 = pd.DataFrame({'M': [10, 11, 12], 'N': [13, 14, 15]})
var0 = 'M'
expected_result =  pd.Series([12, 15], name=2, index=['M', 'N'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'