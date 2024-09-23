df0 = pd.DataFrame({'A': ['x', 'y', 'x'], 'B': ['x', 'z', 'x']})
var0 = 'x'
expected_output = ['A True', 'None False', 'A True']
assert test(df0, var0).equals(pd.Series(expected_output)), 'Test failed'