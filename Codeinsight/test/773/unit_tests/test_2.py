df0 = pd.DataFrame({'A': [1, 2, 3], 'B': ['foo', 'bar', 'foo'], 'C': [True, False, True]})
arg0 = 'B'
arg1 = 'foo'
expected_output = pd.DataFrame({'A': [1, 3], 'B': ['foo', 'foo'], 'C': [True, True]})
assert test(df0, arg0, arg1).columns.equals(expected_output.columns), 'Test failed'