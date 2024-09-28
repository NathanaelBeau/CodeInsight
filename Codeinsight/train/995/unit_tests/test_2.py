matrix0 = np.array([[5, 6], [7, 8]])
expected_result =  np.array([5, 6, 7, 8])
result = test(matrix0)
assert np.array_equal(result, expected_result), 'Test failed'