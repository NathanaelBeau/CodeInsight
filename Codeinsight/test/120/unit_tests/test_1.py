matrix0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
lst1 = [1]
expected_output_1 = np.array([[2], [5], [8]])
assert np.array_equal(test(matrix0, lst1), expected_output_1), 'Test failed'