# Test 2 (Applying str.upper)
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
var0 = 'B'
func = str
expected_result =  pd.Series(['4', '5', '6'], name='B')
result = test(df0, var0, func)
assert result.equals(expected_result), 'Test failed'