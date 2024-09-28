var0 = np.array([[True, True],
                   [False, False]])
expected_output = np.array([[0, 0],
                              [0, 1]])
assert (test(var0)  ==  expected_output).all(), 'Test failed'