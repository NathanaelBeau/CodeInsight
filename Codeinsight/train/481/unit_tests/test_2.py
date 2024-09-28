mat2 = np.array([[-1, -2], [-3, -4]])
expected_result =  np.array([[1, 4], [9, 16]])
result = test(mat2)
assert np.array_equal(result, expected_result), 'Test failed'