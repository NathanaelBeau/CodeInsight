# Test 3
df0 = pd.DataFrame({ 'col1': [10, 20] })
var0 = 'col2'
lst0 = [30, 40]
expected_result =  pd.DataFrame({ 'col1': [10, 20], 'col2': [30, 40] })
assert test(df0.copy(), var0, lst0).equals(expected_result), 'Test failed'