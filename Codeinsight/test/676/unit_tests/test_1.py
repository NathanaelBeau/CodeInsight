arr0 = np.array([[1, 0],
                 [0, 1]])
var0 = 5
expected_output = np.array([[5, 0],
                            [0, 5]])
assert np.array_equal(test(arr0, var0), expected_output), 'Test failed'