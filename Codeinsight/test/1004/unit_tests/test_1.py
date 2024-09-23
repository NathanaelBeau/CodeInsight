df0 = pd.DataFrame({'X': ['x', 'y', 'z'], 'Y': [1, 2, 3]})
df1 = pd.DataFrame({'Z': ['a', 'b', 'c'], 'dates': ['2023-01-01', '2023-02-02', '2023-03-03']})
expected_output = pd.DataFrame({'X': ['x', 'y', 'z'], 'Y': [1, 2, 3], 'dates': ['2023-01-01', '2023-02-02', '2023-03-03']})
assert test(df0, df1) .equals(expected_output), 'Test failed'