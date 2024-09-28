# Test 1
df0 = pd.DataFrame({ 'A': ['x', 'x', 'y', 'y'], 'B': [1, 2, 3, 4] })
var0 = 'A'
var1 = 'B'
expected_result =  pd.Series({ 'x': [1, 2], 'y': [3, 4] }, name='B')
result = test(df0, var0, var1)
assert result.sort_index().equals(expected_result.sort_index()), 'Test failed'