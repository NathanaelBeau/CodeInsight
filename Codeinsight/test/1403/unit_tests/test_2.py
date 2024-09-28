arr0 = np.array([[10, 20], [30, 40], [50, 60]])
vec0 = np.array([10, 20, 30])
expected_result =  np.array([[1, 2], [1.5, 2], [1.66666667, 2]])
result = test(arr0, vec0)
assert np.allclose(result, expected_result), 'Test failed'