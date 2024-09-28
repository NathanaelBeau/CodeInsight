df0 = pd.DataFrame({'A':['a','b', 'c'], 'B':['f', 'g', 'h']}, index=[10,20,30])
var0 = 0
expected_output = 'a'
assert test(df0, var0) ==expected_output, 'Test failed'