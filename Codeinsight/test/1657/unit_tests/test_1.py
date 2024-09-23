# Test 2
df0 = pd.DataFrame({ 'group1': ['A', 'A', 'B', 'B'], 'group2': ['X', 'X', 'Y', 'Y'], 'value': [5, 15, 25, 35] })
var0 = 'group1'
var1 = 'group2'
expected_result =  pd.DataFrame({ 'group1': ['A', 'B'], 'group2': ['X', 'Y'], 'value': [10.0, 30.0] }).set_index(['group1', 'group2'])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'