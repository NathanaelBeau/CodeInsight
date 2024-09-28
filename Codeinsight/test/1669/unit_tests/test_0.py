nvalues = {'A': [1, 2, 3], 'B': [4, 5, 6]}
expected_output = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
assert test(nvalues).equals(expected_output), 'Test failed'