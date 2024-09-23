var0 = np.array([[9, 8, 7, 6, 5],
                   [9, 8, 7, 6, 5],
                   [9, 8, 7, 6, 5],
                   [9, 8, 7, 6, 5]])
expected_output = np.array([6, 5, 6, 5, 6, 5, 6, 5])
assert (test(var0)  == expected_output).all(), 'Test failed'