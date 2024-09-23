# Test 2
df0 = pd.DataFrame({'X': [100, 200], 'Y': [300, 400], 'Z': [500, 600]})
var0 = '^X|Z$'
var1 = 10
expected_result =  pd.DataFrame({'X': [10.0, 20.0], 'Y': [300, 400], 'Z': [50.0, 60.0]})
assert test(df0, var0, var1).equals(expected_result), 'Test failed'