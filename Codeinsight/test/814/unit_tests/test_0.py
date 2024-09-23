var0 = np.array([[True, False, True],
                 [False, True, False],
                 [True, True, False]])
expected_output = np.array([[0, 0],
                            [0, 2],
                            [1, 1],
                            [2, 0],
                            [2, 1]])
assert (test(var0)  ==  expected_output).all(), 'Test failed'