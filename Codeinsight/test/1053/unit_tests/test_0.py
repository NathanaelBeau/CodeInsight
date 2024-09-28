arr1 = np.array([[1, 3], [2, 1], [3, 2]])
expected_1 = np.array([[2, 1], [3, 2], [1, 3]])
assert np.array_equal(test(arr1), expected_1)