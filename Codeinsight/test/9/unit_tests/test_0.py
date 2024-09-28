df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df1 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
expected_output = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12]})
assert test(df0, df1) .equals(expected_output), 'Test failed'