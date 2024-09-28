df0 = pd.DataFrame({'group': ['A', 'A', 'B', 'B', 'B', 'C', 'C'], 'value': [1, 2, 3, 4, 5, 6, 7]})
col_name = 'group'
var0 = 1
result = test(df0, col_name, var0)
assert result['group'].value_counts().max() == var0, 'Test failed'