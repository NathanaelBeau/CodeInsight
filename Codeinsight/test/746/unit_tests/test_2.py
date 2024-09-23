# Test 3 (Applying a lambda function to check if number is even)
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
var0 = 'A'
func = lambda x: x % 2 == 0
expected_result =  pd.Series([False, True, False], name='A')
result = test(df0, var0, func)
assert result.equals(expected_result), 'Test failed'