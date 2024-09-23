# Test 1
mat0 = np.array([[1, 2], [3, 4], [5, 6]])
expected_result =  np.array([2.23606798, 5., 7.81024968])  # Norms of each row
result = test(mat0)
assert np.allclose(result, expected_result), 'Test failed'