df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df1 = pd.DataFrame({'C': ['a', 'b', 'c'], 'dates': ['2023-01-01', '2023-02-02', '2023-03-03']})
expected_output = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'dates': ['2023-01-01', '2023-02-02', '2023-03-03']})
assert test(df0, df1) .equals(expected_output), 'Test failed'