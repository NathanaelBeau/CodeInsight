arr1 = np.array([[3, 2, 1], [1, 3, 2], [2, 1, 3]])
expected1 = np.array([[1, 3, 2], [2, 1, 3], [3, 2, 1]])
assert np.array_equal(test(arr1), expected1), 'Test failed'