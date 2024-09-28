var0 = np.array([3, 1, 4, 1, 5, 1])
expected_output = np.array([1, 3, 5])
assert (test(var0)  == expected_output).all(), 'Test failed'