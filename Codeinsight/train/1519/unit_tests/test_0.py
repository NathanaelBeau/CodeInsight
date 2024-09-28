df0 = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
expected_output = True
assert test(df0) ==expected_output, 'Test failed'