# Test 3
df0 = pd.DataFrame({ 'col1': [10, 20, 30], 'col2': [40, 50, 60] })
var0 = 'col2'
expected_result =  pd.DataFrame({ 'col1': [10, 20, 30] })
assert test(df0.copy(), var0).equals(expected_result), 'Test failed'