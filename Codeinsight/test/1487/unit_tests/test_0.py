df0 = pd.DataFrame({'values': [0.5, 1.2, 2.0, 0.8, 1.5]})
var0 = 'values'
var1 = 1.0
var2 = 2.0
expected_output = [False, True, True, False, True]
assert (test(df0, var0, var1, var2) ==expected_output).all(), 'Test failed'