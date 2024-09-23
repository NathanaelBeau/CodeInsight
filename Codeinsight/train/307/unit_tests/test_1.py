# Test 2
df0 = pd.DataFrame({ 'colors': [['red', 'blue'], ['red'], ['blue', 'green']] })
col0 = 'colors'
expected_result = pd.DataFrame({ 'blue': [1, 0, 1], 'green': [0, 0, 1], 'red': [1, 1, 0] })
result = test(df0, col0)
assert result.equals(expected_result), 'Test failed'