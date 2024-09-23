A = np.array([[0.2, 0.4], [0.1, 0.5], [0.3, 0.3]])
expected_output = np.array([[0.1, 0.3], [0.2, 0.4], [0.3, 0.5]])
assert np.array_equal(test(A), expected_output), 'Test failed'