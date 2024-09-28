matrix0 = np.array([[1, 2], [3, 4], [5, 6]])
expected_result =  np.array([np.sqrt(5), np.sqrt(25), np.sqrt(61)])
result = test(matrix0)
assert np.array_equal(result, expected_result), 'Test failed'