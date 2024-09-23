arr0 = np.array([0, 1, 2, 3, 0, 4, 5])
expected_output = np.array([1, 2, 3, 4, 5])
assert np.array_equal(test(arr0), expected_output), 'Test failed'