df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
var0 = ['A', 'B']
expected_output = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
assert test(df0, df1, var0) .equals( expected_output), 'Test failed'