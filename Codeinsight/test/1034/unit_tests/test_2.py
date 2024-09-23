arr0 = np.array([10, 20, 30, 40, 50])
var0 = 15
var1 = 35
expected_output = (np.array([1, 2]),)
assert np.array_equal(test(arr0, var0, var1), expected_output), 'Test failed'