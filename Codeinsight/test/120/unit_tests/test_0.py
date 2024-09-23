matrix0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
lst0 = [0, 2]
expected_output_0 = np.array([[1, 3], [4, 6], [7, 9]])
assert np.array_equal(test(matrix0, lst0), expected_output_0), 'Test failed'