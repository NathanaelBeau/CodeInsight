# Test 1 (Applying a lambda function to square the values)
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
var0 = 'A'
func = lambda x: x**2
expected_result =  pd.Series([1, 4, 9], name='A')
result = test(df0, var0, func)
assert result.equals(expected_result), 'Test failed'