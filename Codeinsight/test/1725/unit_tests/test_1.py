df0 = pd.DataFrame({ 'column_name': [15, 25, 30, 45, 55], 'other_column': ['X', 'Y', 'Z', 'W', 'Q'] })
var0 = 'column_name'
var1 = 25
expected_output = df0.loc[df0[var0] == var1]
assert test(df0,var0, var1) .equals(expected_output), 'Test failed'