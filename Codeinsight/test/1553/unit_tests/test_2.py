arr0 = np.array([[0, 0, 0], [0, 0, 0]])
var0 = 1
expected_output = (np.array([], dtype=int), np.array([], dtype=int))
output = test(arr0, var0)
assert np.array_equal(output[0], expected_output[0]) and np.array_equal(output[1], expected_output[1]), 'Test failed'