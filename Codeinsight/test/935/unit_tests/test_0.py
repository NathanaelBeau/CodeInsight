arr0 = np.array([0, 1, 2, 3, 4, 5])
var0 = 0
var1 = 1
expected_output_0 = np.array([0., 0.2, 0.4, 0.6, 0.8, 1.])
assert np.allclose(test(arr0, var0, var1), expected_output_0), 'Test failed'