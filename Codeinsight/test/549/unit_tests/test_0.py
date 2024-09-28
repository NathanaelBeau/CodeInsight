var0 = 'group_column'
var1 = 'value_column'
df0 = pd.DataFrame({ 'group_column': ['A', 'A', 'B', 'B', 'C'], 'value_column': [1, 1, 2, 3, 4] })
expected_result =  pd.Series([1, 2, 1], index=['A', 'B', 'C'])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'