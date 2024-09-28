df0 = pd.DataFrame({'values': [0.2, 0.8, 3.0, 1.5, 2.5]})
var0 = 'values'
var1 = 1.0
var2 = 2.0
expected_output = [False, False, False, True, False]
assert (test(df0, var0, var1, var2) ==expected_output).all(), 'Test failed'