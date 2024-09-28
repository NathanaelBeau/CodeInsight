df1 = pd.DataFrame({ 'a': [1, 2, 3], 'b': [4, 5, 6], 'x': [7, 8, 9], 'y': [10, 11, 12] })
expected_output1 = pd.DataFrame({ 'x': [7, 8, 9], 'y': [10, 11, 12], 'a': [1, 2, 3], 'b': [4, 5, 6] })
assert test(df1).equals(expected_output1), 'Test failed'