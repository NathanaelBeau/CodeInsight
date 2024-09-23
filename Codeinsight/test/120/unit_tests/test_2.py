matrix0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
lst2 = [0, 1, 2]
expected_output_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
assert np.array_equal(test(matrix0, lst2), expected_output_2), 'Test failed'