arr0 = np.array([[1, 2, 3], [4, 5, 6]])
var0 = 5
expected_output = (np.array([1]), np.array([1]))
output = test(arr0, var0)
assert np.array_equal(output[0], expected_output[0]) and np.array_equal(output[1], expected_output[1]), 'Test failed'