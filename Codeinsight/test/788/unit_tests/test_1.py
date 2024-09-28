df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
arg0 = 'B'
arg1 = 20
expected_output = pd.DataFrame({'A': [2], 'B': [20]})
assert test(df0, arg0, arg1).columns.equals(expected_output.columns), 'Test failed'