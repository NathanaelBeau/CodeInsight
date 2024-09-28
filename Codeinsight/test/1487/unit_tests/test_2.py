df0 = pd.DataFrame({'values': [2.5, 3.0, 4.0, 1.2, 0.5]})
var0 = 'values'
var1 = 2.0
var2 = 3.0
expected_output = [True, True, False, False, False]
assert (test(df0, var0, var1, var2) == expected_output).all(), 'Test failed'