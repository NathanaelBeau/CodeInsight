# Test 2
df0 = pd.DataFrame({ 'X': ['0.5', '1.5', '2.5'] })
var0 = 'X'
var1 = 'float64'
expected_result =  pd.DataFrame({ 'X': [0.5, 1.5, 2.5] })
assert test(df0.copy(), var0, var1).equals(expected_result), 'Test failed'