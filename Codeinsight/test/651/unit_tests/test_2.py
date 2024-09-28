df0 = pd.DataFrame({ 'group1': ['A', 'B', 'A', 'B'], 'group2': ['X', 'Y', 'X', 'Y'], 'value': [50, 60, 70, 80] })
var0 = 'group1'
var1 = 'group2'
expected_result =  pd.DataFrame({ 'group1': ['A', 'B'], 'group2': ['X', 'Y'], 'value': [60.0, 70.0] }).set_index(['group1', 'group2'])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'