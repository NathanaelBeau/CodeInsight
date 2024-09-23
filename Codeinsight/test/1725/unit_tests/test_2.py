df0 = pd.DataFrame({ 'column_name': [8, 18, 28, 38, 48], 'other_column': ['P', 'Q', 'R', 'S', 'T'] })
var0 = 'column_name'
var1 = 8
expected_output = df0.loc[df0[var0] == var1]
assert test(df0,var0, var1) .equals(expected_output), 'Test failed'