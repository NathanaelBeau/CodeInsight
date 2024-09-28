matrix0 = np.array([[1, 2], [3, 4]])
expected_result =  np.linalg.inv(np.array([[1, 2], [3, 4]]))
result = test(matrix0)
assert np.allclose(result, expected_result), 'Test failed'