mat0 = np.array([[4, -2], [1, 1]])
expected_eigenvalues = np.array([3., 2.])
result_eigenvalues, _ = test(mat0)
assert np.allclose(result_eigenvalues, expected_eigenvalues), 'Test failed'