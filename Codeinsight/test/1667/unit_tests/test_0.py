# Test 1
df0 = pd.DataFrame({ 'A': ['1', '2', '3'] })
var0 = 'A'
var1 = 'int64'
expected_result =  pd.DataFrame({ 'A': [1, 2, 3] })
assert test(df0.copy(), var0, var1).equals(expected_result), 'Test failed'