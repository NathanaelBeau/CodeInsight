df0 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [True, False, True]})
var0 = 'B'
expected_output = pd.DataFrame({'A': [1, 2, 3], 'C': [True, False, True]})
assert test(df0, var0) .equals(expected_output), 'Test failed'