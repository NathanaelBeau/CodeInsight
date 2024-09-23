A = np.array([[0.9, 0.8], [0.7, 0.6]])
expected_output = np.array([[0.7, 0.6], [0.9, 0.8]])
assert np.array_equal(test(A), expected_output), 'Test failed'