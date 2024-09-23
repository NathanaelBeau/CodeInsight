arr0 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
var0 = 3
var1 = 7
expected_output = (np.array([2, 3, 4, 5, 6]),)
assert np.array_equal(test(arr0, var0, var1), expected_output), 'Test failed'