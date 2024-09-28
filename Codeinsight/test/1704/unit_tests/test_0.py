df0 = pd.DataFrame({'var0': [1, 2, 3, 1, 4], 'b': [10, 20, 30, 40, 50]})
var0 = 1
expected_output = 50
assert test(df0, var0) ==expected_output, 'Test failed'