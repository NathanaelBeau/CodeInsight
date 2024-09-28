arr0 = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3])
var0 = -3
var1 = 2
expected_output = (np.array([2, 3, 4, 5, 6, 7]),)
assert np.array_equal(test(arr0, var0, var1), expected_output), 'Test failed'