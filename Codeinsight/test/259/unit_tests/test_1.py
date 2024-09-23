x2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
var0_2 = 1
expected_output2 = np.array([[1, 2, 3], [7, 8, 9]])
assert np.array_equal(test(x2, var0_2), expected_output2), 'Test failed'