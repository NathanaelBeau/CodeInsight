var0 = np.array([[False, True, False],
                   [True, False, True]])
expected_output = np.array([[0, 1],
                              [1, 0],
                              [1, 2]])
assert (test(var0)  ==  expected_output).all(), 'Test failed'