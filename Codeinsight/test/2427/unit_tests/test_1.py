df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_output = False
assert test(df0) ==expected_output, 'Test failed'