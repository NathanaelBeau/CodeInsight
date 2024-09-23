arr0 = np.array([[3.14, 2.71],
                 [1.618, 0.577]])
var0 = 42
expected_output = np.array([[42.0, 2.71],
                            [1.618, 42.0]])
assert np.array_equal(test(arr0, var0), expected_output), 'Test failed'