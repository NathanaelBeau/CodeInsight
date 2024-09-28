var0 = np.array([1, 2, 3, 4, 5])
expected_output = np.array([1, 4, 5, 5, 5])
assert (test(var0)  == expected_output).all(), 'Test failed'