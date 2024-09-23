df0 = pd.DataFrame({ 'column_name': [10, 20, 30, 40, 50], 'other_column': ['A', 'B', 'C', 'D', 'E'] })
var0 = 'column_name'
var1 = 30
expected_output = df0.loc[df0[var0] == var1]
assert test(df0,var0, var1) .equals(expected_output), 'Test failed'