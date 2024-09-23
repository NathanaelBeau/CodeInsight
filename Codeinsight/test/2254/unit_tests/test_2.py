arr3 = np.array([[1, 2, 3], [1, 2, 3], [2, 2, 2]])
expected3 = np.array([[1, 2, 3], [1, 2, 3], [2, 2, 2]])
assert np.array_equal(test(arr3), expected3), 'Test failed'