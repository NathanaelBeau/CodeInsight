# Test 1
df0 = pd.DataFrame({ 'A': ['x', 'x', 'y', 'y', 'y'] })
var0 = 'A'
expected_result =  pd.Series({'y': 3, 'x': 2}, name='A')
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'