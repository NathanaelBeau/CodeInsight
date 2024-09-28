matrix0 = np.array([[9, 10], [11, 12]])
expected_result =  np.array([9, 10, 11, 12])
result = test(matrix0)
assert np.array_equal(result, expected_result), 'Test failed'