# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3, 4]})
var0 = 'A'
expected_result =  pd.Series([4], name=3, index=['A'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'