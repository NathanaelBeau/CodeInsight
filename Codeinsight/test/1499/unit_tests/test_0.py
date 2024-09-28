df0 = pd.DataFrame({ 'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8] }, index=['x', 'x', 'y', 'y'])
expected_output = pd.DataFrame({ 'A': [3, 7], 'B': [11, 15] }, index=['x', 'y'])
assert test(df0).equals(expected_output), 'Test failed'