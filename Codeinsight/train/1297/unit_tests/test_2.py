df = pd.DataFrame({ 'A': [0, 0, 0, 0, 0], 'B': [1, 2, 3, 4, 5] })
expected_output = pd.DataFrame({ 'A': [0, 0, 0, 0, 0], 'B': [np.nan, np.nan, np.nan, np.nan, np.nan] })
assert test(df).equals(expected_output), 'Test failed'