df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
expected_output1 = pd.DataFrame({'A': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2], 'B': [3, 3, 3, 3, 3, 4, 4, 4, 4, 4]})
assert test(df1, 5).equals(expected_output1), 'Test failed'