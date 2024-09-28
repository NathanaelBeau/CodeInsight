df1 = pd.DataFrame({ 'A': [3, 1, 2], 'B': [2, 3, 1], 'C': [1, 2, 3] })
expected_output1 = pd.DataFrame({ 'A': [3, 3, 3], 'B': [2, 2, 2], 'C': [1, 1, 1] })
assert test(df1).equals(expected_output1), 'Test failed'