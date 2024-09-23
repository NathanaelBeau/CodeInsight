df0 = pd.DataFrame({'Col1': [1, 2, 3], 'Col2': [4, 5, 6]})
df1 = pd.DataFrame({'Col1': [1, 2, 3], 'Col2': [4, 5, 6], 'Col3': [7, 8, 9]})
var0 = ['Col1', 'Col2']
expected_output = pd.DataFrame({'Col1': [1, 2, 3], 'Col2': [4, 5, 6]})
assert test(df0, df1, var0) .equals( expected_output), 'Test failed'