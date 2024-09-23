var0 = np.array([0, 0, 0, 0, 0, 0])
expected_output = np.array([0, 2, 2, 1, 0, 0])
assert (test(var0)  == expected_output).all(), 'Test failed'