x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
var0_3 = 2
expected_output3 = np.array([[1, 2, 3], [4, 5, 6]])
assert np.array_equal(test(x3, var0_3), expected_output3), 'Test failed'