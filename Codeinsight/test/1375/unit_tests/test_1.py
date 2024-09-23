arr0 = np.array([[True, False], [True, True]])
expected_result =  (np.array([0, 1, 1]), np.array([0, 0, 1]))
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'