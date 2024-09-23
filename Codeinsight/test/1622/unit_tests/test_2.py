arr0 = np.array([-2, -1, 0, 1, 2])
expected_output = np.array([[ 0, -2,  0,  0, 0],
                            [ 0, -1,  0,  1,  0],
                            [ 0,  0,  0 , 2,  0]])
assert np.array_equal(test(arr0), expected_output), 'Test failed'