arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
expected2 = arr2  # Already sorted
assert np.array_equal(test(arr2), expected2), 'Test failed'