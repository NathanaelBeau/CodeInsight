var0 = np.array([1, 2, 2, 1, 3])
expected_output = np.array([1, 4, 4, 2, 3])
assert (test(var0)  == expected_output).all(), 'Test failed'