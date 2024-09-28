arr0 = np.array([[1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1]])
var0 = 1
expected_output = np.array([[0, 0],
                            [0, 1],
                            [0, 2],
                            [0, 3],
                            [1, 0],
                            [1, 1],
                            [1, 2],
                            [1, 3],
                            [2, 0],
                            [2, 1],
                            [2, 2],
                            [2, 3]])
output = test(arr0, var0)
assert np.array_equal(output, expected_output), 'Test failed'