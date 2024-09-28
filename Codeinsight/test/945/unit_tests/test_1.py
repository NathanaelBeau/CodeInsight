matrix0 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
vec0 = np.array([10, 40, 70])
expected_result =  np.array([[0, 10, 20], [0, 10, 20], [0, 10, 20]])
result = test(matrix0, vec0)
assert np.array_equal(result, expected_result), 'Test failed'