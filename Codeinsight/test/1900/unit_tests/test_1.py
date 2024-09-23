df0 = pd.DataFrame({ 'X': ['cat', 'cat', 'dog'], 'Y': [7, 8, 9], 'Z': ['m', 'n', 'o'] })
var0 = 'X'
expected_result2 = pd.DataFrame({ 'X': ['cat', 'dog'], 'Y': [7, 9], 'Z': ['m', 'o'] })
result2 = test(df0, var0)
assert result2.equals(expected_result2), 'Test failed'