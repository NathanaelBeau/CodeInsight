df0 = pd.DataFrame({ 'M': ['red', 'blue', 'red'], 'N': [10, 11, 12], 'O': ['a', 'b', 'c'] })
var0 = 'M'
expected_result3 = pd.DataFrame({ 'M': ['blue', 'red'], 'N': [11, 10], 'O': ['b', 'a'] })
result3 = test(df0, var0)
assert result3.equals(expected_result3), 'Test failed'