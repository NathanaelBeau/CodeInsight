arr0 = np.array([[0, 1, 2, 3],
                 [1, 1, 1, 1],
                 [2, 3, 4, 5]])
var0 = 1
expected_output = np.array([[0, 1],
                            [1, 0],
                            [1, 1],
                            [1, 2],
                            [1, 3]])
output = test(arr0, var0)
assert np.array_equal(output, expected_output), 'Test failed'