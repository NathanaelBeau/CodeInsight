df0 = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})
df1 = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6], 'Z': [7, 8, 9]})
var0 = ['X', 'Y']
expected_output = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})
assert test(df0, df1, var0) .equals( expected_output), 'Test failed'