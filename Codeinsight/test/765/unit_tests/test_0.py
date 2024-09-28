arr0 = np.array([0, 2, 1])
var0 = 3
expected_result =  np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'