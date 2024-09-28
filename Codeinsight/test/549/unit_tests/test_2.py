var0 = 'group_column'
var1 = 'value_column'
df0 = pd.DataFrame({ 'group_column': ['P', 'P', 'Q', 'Q', 'R', 'R'], 'value_column': [9, 9, 10, 10, 11, 12] })
expected_result =  pd.Series([1, 1, 2], index=['P', 'Q', 'R'])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'