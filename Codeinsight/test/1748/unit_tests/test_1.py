df0 = pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['x', 'y', 'z']})
var0 = 'x'
expected_output = ['Y True', 'None False', 'None False']
assert test(df0, var0).equals(pd.Series(expected_output)), 'Test failed'