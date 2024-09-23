nvalues = {'X': [5, 6, 7], 'Y': [8, 9, 10], 'Z': [11, 12, 13]}
expected_output = pd.DataFrame({'X': [5, 6, 7], 'Y': [8, 9, 10], 'Z': [11, 12, 13]})
assert test(nvalues).equals(expected_output), 'Test failed'