# Test 3
df0 = pd.DataFrame({'Type': ['alpha', 'beta', 'alpha', 'gamma', 'gamma'], 'Data': ['one', 'one', 'two', 'two', 'three']})
var0 = 'Type'
var1 = 'Data'
expected_result =  pd.Series([2, 1, 2], index=['alpha', 'beta', 'gamma'], name='Data')
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'