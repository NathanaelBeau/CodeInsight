df0 = pd.DataFrame({ 'A': [1, 5], 'B': [3, 7], 'C': [5, 9], 'D': [7, 11], 'E': [9, 13], 'F': [11, 15] })
expected_output = pd.DataFrame({ 0: [3.0, 7.0], 1: [9.0, 13.0] })
assert test(df0).equals(expected_output), 'Test failed'