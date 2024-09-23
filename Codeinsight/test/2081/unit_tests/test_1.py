matrix0 = np.array([[4, 7], [2, 6]])
expected_result =  np.linalg.inv(np.array([[4, 7], [2, 6]]))
result = test(matrix0)
assert np.allclose(result, expected_result), 'Test failed'