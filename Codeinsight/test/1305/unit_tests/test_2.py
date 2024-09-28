mat0 = np.array([[2, 1], [1, 3]])
expected_eigenvalues = np.array([3.61803399, 1.38196601])
result_eigenvalues, _ = test(mat0)
assert np.allclose(result_eigenvalues, expected_eigenvalues), 'Test failed'