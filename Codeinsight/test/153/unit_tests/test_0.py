x1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
var0_1 = 0
expected_output1 = np.array([[4, 5, 6], [7, 8, 9]])
assert np.array_equal(test(x1, var0_1), expected_output1), 'Test failed'