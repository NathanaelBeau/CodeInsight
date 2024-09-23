var0 = 'group_column'
var1 = 'value_column'
df0 = pd.DataFrame({ 'group_column': ['X', 'X', 'Y', 'Y', 'Z'], 'value_column': [5, 6, 6, 7, 8] })
expected_result =  pd.Series([2, 2, 1], index=['X', 'Y', 'Z'])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'