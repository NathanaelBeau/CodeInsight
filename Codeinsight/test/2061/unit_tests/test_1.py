df = pd.DataFrame({ 'A': [10, 20, 30, 0, 50], 'B': [55, 66, 77, 88, 99] })
expected_output = pd.DataFrame({ 'A': [10, 20, 30, 0, 50], 'B': [55, 66, 77, np.nan, 99] })
assert test(df).equals(expected_output), 'Test failed'