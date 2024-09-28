matrix0 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
expected_result =  np.linalg.inv(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
result = test(matrix0)
assert np.allclose(result, expected_result), 'Test failed'