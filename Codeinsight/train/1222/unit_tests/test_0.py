# Test 1
df0 = pd.DataFrame({ 'A': [3, 1, 2], 'B': [30, 10, 20] })
var0 = 'A'
expected_result =  pd.DataFrame({ 'A': [1, 2, 3], 'B': [10, 20, 30] }, index=[1,2,0])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'