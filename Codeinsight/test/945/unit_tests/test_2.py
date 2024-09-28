matrix0 = np.array([[0.5, 1.0], [1.5, 2.0], [2.5, 3.0]])
vec0 = np.array([0.5, 1.5, 2.5])
expected_result =  np.array([[0, 0.5], [0, 0.5], [0, 0.5]])
result = test(matrix0, vec0)
assert np.array_equal(result, expected_result), 'Test failed'