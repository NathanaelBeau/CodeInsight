arr0 = np.array([2, 3, 5])
arr1 = np.array([0, 1, 2])
expected_output = np.array([[ 0,  2,  4],
                            [ 0,  3,  6],
                            [ 0,  5, 10]])
assert (test(arr0, arr1)  == expected_output).all(), 'Test failed'