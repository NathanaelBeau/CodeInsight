matrix0 = np.array([[0, 0], [0, 0], [0, 0]])
expected_result =  np.array([0, 0, 0])
result = test(matrix0)
assert np.array_equal(result, expected_result), 'Test failed'