df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [10, 20], 'B': [30, 40]})
expected_output = pd.DataFrame({'A': [10, 40], 'B': [90, 160]})
assert test(df1, df2).equals(expected_output), 'Test failed'