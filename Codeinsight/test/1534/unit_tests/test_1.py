df0 = pd.DataFrame({ 'A': [5, 10], 'B': [15, 20], 'C': [25, 30], 'D': [35, 40], 'E': [45, 50], 'F': [55, 60] })
expected_output = pd.DataFrame({ 0: [15.0, 20.0], 1: [45.0, 50.0] })
assert test(df0).equals(expected_output), 'Test failed'