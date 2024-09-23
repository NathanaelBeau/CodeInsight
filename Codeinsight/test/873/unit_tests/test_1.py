mat0 = np.array([[6, 2], [2, 3]])
expected_eigenvalues = np.array([7., 2.])
result_eigenvalues, _ = test(mat0)
assert np.allclose(result_eigenvalues, expected_eigenvalues), 'Test failed'