df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df1 = pd.DataFrame({'A': [2, 2, 2], 'B': [2, 2, 2]})
expected_output = pd.DataFrame({'A': [2, 4, 6], 'B': [8, 10, 12]})
assert test(df0, df1).equals(expected_output), 'Test failed'