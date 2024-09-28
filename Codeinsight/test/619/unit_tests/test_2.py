A = np.array([[1.2, 1.1], [1.3, 1.4], [1.1, 1.2]])
expected_output = np.array([[1.1, 1.1], [1.2, 1.2], [1.3, 1.4]])
assert np.array_equal(test(A), expected_output), 'Test failed'