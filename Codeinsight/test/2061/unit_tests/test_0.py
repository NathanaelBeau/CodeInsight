df = pd.DataFrame({ 'A': [0, 1, 2, 0, 4], 'B': [5, 6, 7, 8, 9] })
expected_output = pd.DataFrame({ 'A': [0, 1, 2, 0, 4], 'B': [np.nan, 6, 7, np.nan, 9] })
assert test(df).equals(expected_output), 'Test failed'