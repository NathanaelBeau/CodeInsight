var0 = np.array([[0, 1, 2, 3, 4],
                 [0, 1, 2, 3, 4],
                 [0, 1, 2, 3, 4],
                 [0, 1, 2, 3, 4]])
expected_output = np.array([3, 4, 3, 4, 3, 4, 3, 4])
assert (test(var0)  == expected_output).all(), 'Test failed'