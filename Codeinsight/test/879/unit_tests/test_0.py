data = np.array([[1, 2, np.nan], [4, 5, 6], [np.nan, np.nan, 9]])
expected_output = 6
assert test(data) == expected_output, 'Test failed'