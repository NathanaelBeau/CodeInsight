# Test 1
df0 = pd.DataFrame({'Group': ['A', 'A', 'B', 'B', 'B'], 'Value': [1, 1, 2, 2, 3]})
var0 = 'Group'
var1 = 'Value'
expected_result =  pd.Series([1, 2], index=['A', 'B'], name='Value')
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'