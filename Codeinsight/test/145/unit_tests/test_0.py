df0 = pd.DataFrame({'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']})
var0 = 'column1'
expected_output = pd.DataFrame({'column2': ['a', 'b', 'c']})
assert test(df0, var0) .equals(expected_output), 'Test failed'