df0 = pd.DataFrame({'A': ['x', 'y', 'z'], 'B': ['p', 'q', 'r']})
var0 = 'x'
expected_output = ['A True', 'None False', 'None False']
assert test(df0, var0).equals(pd.Series(expected_output)), 'Test failed'