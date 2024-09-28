df0 = pd.DataFrame({'A': [np.nan, 2, 3], 'B': [4, 5, 6]})
expected_output = True
assert test(df0) ==expected_output, 'Test failed'