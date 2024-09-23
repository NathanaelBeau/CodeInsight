arr0 = np.array([[11, 12, 13],
                   [21, 22, 23],
                   [31, 32, 33],
                   [41, 42, 43]])
expected_output = np.array([[11, 12, 13],
                              [21, 22, 23],
                              [31, 32, 33],
                              [41, 42, 43]])
assert (test(arr0)  == expected_output).all(), 'Test failed'