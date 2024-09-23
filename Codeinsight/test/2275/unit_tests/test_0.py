arr0 = np.array([0, 1, 2, 3, 4])
arr1 = np.array([5, 6, 7])
expected_output = np.array([[ 0,  0,  0],
                            [ 5,  6,  7],
                            [10, 12, 14],
                            [15, 18, 21],
                            [20, 24, 28]])
assert (test(arr0, arr1)  == expected_output).all(), 'Test failed'