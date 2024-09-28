df1 = pd.DataFrame({'type': ['X', 'X', 'Y', 'Y', 'Z', 'Z'], 'value': [10, 11, 12, 13, 14, 15]})
col_name = 'type'
var1 = 2
result = test(df1, col_name, var1)
assert result['type'].value_counts().max() == var1, 'Test failed'