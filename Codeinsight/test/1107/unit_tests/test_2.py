df0 = pd.DataFrame({'var0': [2, 3, 4], 'b': [20, 30, 40]})
var0 = 1
expected_output = 0
assert test(df0, var0) ==expected_output, 'Test failed'