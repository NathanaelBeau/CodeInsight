df0 = pd.DataFrame({'A':['x','y', 'z'], 'B':['m', 'n', 'o']}, index=[100, 200, 300])
var0 = 2
expected_output = 'z'
assert test(df0, var0) ==expected_output, 'Test failed'