# Test 3
mat0 = np.array([[1, 1], [1, 1], [1, 1]])
expected_result =  np.array([1.41421356, 1.41421356, 1.41421356])  # Norms of each row
result = test(mat0)
assert np.allclose(result, expected_result), 'Test failed'