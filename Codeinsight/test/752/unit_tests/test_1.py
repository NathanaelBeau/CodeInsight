arr0 = np.array([[1.0, 2.0, np.nan], [4.0, np.nan, 6.0]])
expected_output = np.array([[0, 2], [1, 1]])
assert np.array_equal(test(arr0), expected_output), 'Test failed'