arr0 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
var0 = 0
expected_output = np.array([[0, 2, 3],
                            [4, 0, 6],
                            [7, 8, 0]])
assert np.array_equal(test(arr0, var0), expected_output), 'Test failed'