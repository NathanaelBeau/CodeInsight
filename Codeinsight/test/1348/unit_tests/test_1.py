# Test 2
mat0 = np.array([[0, 3], [4, 0], [0, 0]])
expected_result =  np.array([3., 4., 0.])  # Norms of each row
result = test(mat0)
assert np.allclose(result, expected_result), 'Test failed'